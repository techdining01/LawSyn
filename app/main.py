import json
from datetime import datetime
from fastapi import FastAPI, Request, Form, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

# Business Logic Imports
from app.core.jurisdiction import JURISDICTION_DATA
from app.database import SessionLocal, Case
from app.services.scraper_factory import ScraperFactory
from app.ai_agent import parse_court_data
from app.worker import morning_judicial_sync  

app = FastAPI(title="LawSync National Hub")
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

# --- DASHBOARD & VIEWS ---

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    """The National Hub showing the Big 15 states."""
    return templates.TemplateResponse("dashboard.html", {
        "request": request, 
        "states_data": JURISDICTION_DATA
    })


@app.get("/state/{state_id}", response_class=HTMLResponse)
async def state_detail(request: Request, state_id: str):
    """Deep dive into a specific state's rules and limits."""
    data = JURISDICTION_DATA.get(state_id.lower())
    if not data:
        raise HTTPException(status_code=404, detail="State not integrated.")
    return templates.TemplateResponse("state_view.html", {
        "request": request,
        "state": data
    })


@app.post("/sync-case")
async def sync_case(request: Request, suit_no: str = Form(...), state: str = Form(...)):
    """
    THE PRIMARY ENGINE: 
    1. Scrapes Live Data
    2. Parses with AI
    3. Saves to DB
    4. Renders Section 84 Cert
    """
    db = SessionLocal()
    try:
        # 1. LIVE SCRAPE (Factory decides if it's Lagos, Abuja, or Oyo)
        raw_text = ScraperFactory.get_data(state, suit_no)

        # 2. AI PARSING (Gemini 2.0 Flash)
        case_info = parse_court_data(raw_text)

        # 3. DATABASE PERSISTENCE
        new_case = Case(
            suit_no=suit_no,
            state=state,
            claimant=case_info.get('claimant', 'N/A'),
            defendant=case_info.get('defendant', 'N/A'),
            last_status=case_info.get('status', 'Active'),
            updated_at=datetime.utcnow()
        )
        db.merge(new_case) # Update if exists, Create if not
        db.commit()

        # 4. RENDER SECTION 84 CERTIFICATE
        cert_payload = {
            "state": state.upper(),
            "case_id": suit_no,
            "claimant": case_info.get('claimant'),
            "defendant": case_info.get('defendant'),
            "device": "LAWSYNC-PRO-NODE-01",
            "date": datetime.now().strftime("%B %d, %Y"),
            "declaration": f"Case record verified via {state.title()} Judicial Portal."
        }
        return templates.TemplateResponse("certificate.html", {"cert": cert_payload})
    
    finally:
        db.close()

@app.post("/trigger-global-sync")
async def trigger_global_sync():
    """Triggers the background worker to scan all cases in the DB."""
    morning_judicial_sync.delay()
    return {"message": "Background Morning Watch has been initiated."}