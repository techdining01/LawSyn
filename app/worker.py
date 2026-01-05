from celery import Celery
# from .scraper_logic import selenium_search_lagos
from app.ai_agent import client, generate_legal_alert
from app.scraper_logic import scrape_court_status, save_to_database
from app.notifications import send_invasive_alert
from app.core.jurisdiction import get_state_rules
from app.services.scraper import scrape_lagos_case
from app.ai_agent import extract_case_details, generate_legal_alert
from app.services.notifier import send_invasive_update
from app.pdf_generator import create_pdf_certificate



celery_app = Celery('lawsync_tasks', broker='redis://localhost:6379/0')



@celery_app.task
def morning_court_watch():
    # 1. Pull active cases from your database
    # cases = db.query(Case).filter(Case.status == 'active').all()
    mock_cases = [{"suit_no": "LD/999/CIV", "email": "lawyer@chambers.com", "state": "lagos"}]

    for case in mock_cases:
        # A. Scrape the live court portal
        raw_text = scrape_lagos_case(case['suit_no'])
        
        # B. Check if status has changed (Logic: compare with last known status in DB)
        ai_insight = generate_legal_alert(case['state'], raw_text)
        
        # C. Generate the Professional PDF we redid
        # (Using the layout with the Double Border and Times New Roman)
        pdf_bytes = create_pdf_certificate(raw_text) 
        
        # D. PUSH to the lawyer
        send_invasive_update(case['email'], case['suit_no'], ai_insight, pdf_bytes)
    

@celery_app.task
def morning_sync_task(state_id, suit_no, lawyer_email):
    # 1. Scrape
    status = scrape_court_status(state_id, suit_no)
    
    # 2. AI Analysis
    ai_insight = generate_legal_alert(state_id, status)
    
    # 3. Save
    save_to_database(state_id, suit_no, status, ai_insight)
    
    # 4. Notify
    send_invasive_alert(lawyer_email, {"suit_no": suit_no, "state": state_id}, ai_insight)
    
    return "Task Completed Successfully"


@celery_app.task
def sync_and_alert_task(state_id, suit_no, lawyer_email):
    state_info = get_state_rules(state_id)
    rules_context = state_info.get("rules", "Standard rules apply.")
    
    # We pass the specific state rules to Gemini
    ai_insight = generate_legal_alert(state_id, f"Rules: {rules_context}. Status: Scraped data here.")
    
    # # 3. NOTIFY
    send_invasive_alert(lawyer_email, {"suit_no": suit_no, "state": state_id, "status": scrape_court_status(state_id, suit_no)}, ai_insight)
    
    return "SUCCESS: Loop Completed."
