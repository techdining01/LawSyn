import json
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from .worker import morning_sync_task
from app.core.jurisdiction import JURISDICTION_DATA
from fastapi.responses import Response
from app.pdf_generator import create_pdf_certificate
from app.services.scraper import scrape_lagos_case
from app.ai_agent import extract_case_details



app = FastAPI()
templates = Jinja2Templates(directory="templates")

# 1. Mount static files (for CSS/JS)
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/")
async def home(request: Request):
    return templates.TemplateResponse("dashboard.html", {
        "request": request, 
        "states_data": JURISDICTION_DATA # All the deep detail is now here
    })

@app.post("/test-sync")
async def test_sync(state: str, suit_no: str, email: str):
    # This triggers the worker we just fixed!
    morning_sync_task.delay(state, suit_no, email)
    return {"message": "Invasive Sync Started"}


# THE NEW DYNAMIC ROUTE
@app.get("/state/{state_id}", response_class=HTMLResponse)
async def state_detail(request: Request, state_id: str):
    # Fetch the specific logic for the chosen state
    data = JURISDICTION_DATA.get(state_id.lower())
    
    return templates.TemplateResponse("state_view.html", {
        "request": request,
        "state": data
    })


@app.get("/generate-cert/{state_id}/{case_id}")
async def generate_certificate(request: Request, state_id: str, case_id: str):
    # Get state name from our Big 15 list
    state_info = JURISDICTION_DATA.get(state_id.lower())
    
    # This is the legal "Boilerplate" required by the Evidence Act
    certificate_content = {
        "case_id": case_id,
        "state": state_info['name'],
        "device": "LawSync Cloud Server (Ubuntu/Python Engine)",
        "declaration": f"The electronic record of Case {case_id} was produced by the LawSync system during a period over which the computer was used regularly to store or process information for the purposes of legal record keeping."
    }
    
    return templates.TemplateResponse("certificate.html", {
        "request": request,
        "cert": certificate_content
    })


@app.post("/force-sync/{state_id}")
async def force_sync(state_id: str):
    # 1. We trigger the Celery task in the background
    # .delay() means "Don't wait for it to finish, just start it"
    task = morning_sync_task.delay(state_id) 
    
    # 2. Redirect the user back to the dashboard with a success message
    return {"message": f"Sync started in background for {state_id}. Task ID: {task.id}"}




@app.get("/generate-cert/lagos/{suit_no}")
async def download_lagos_cert(suit_no: str):
    # 1. Real-time Scrape
    raw_data = scrape_lagos_case(suit_no)
    
    # 2. AI Extraction
    structured_json = extract_case_details(raw_data)
    case_info = json.loads(structured_json)
    
    # 3. Build the Certificate Object for your Professional Layout
    cert_data = {
        "state": "Lagos State",
        "case_id": suit_no,
        "division": "COMMERCIAL",
        "claimant": case_info['claimant'],
        "defendant": case_info['defendant'],
        "device": "LawSync Verified Node-01",
        "lawyer_name": "Counsel In Charge",
        "date": "05/01/2026", # Today's date
        "declaration": f"The case was identified as a {case_info['last_event']} event."
    }
    
    return templates.TemplateResponse("certificate.html", {"cert": cert_data})