import os
from celery import Celery
from app.database import SessionLocal, Case
from app.services.scraper_factory import ScraperFactory
from app.ai_agent import parse_court_data
from app.services.notifier import send_telegram_alert, send_formal_notification
from app.pdf_generator import create_pdf_certificate


# Initialize Celery
celery_app = Celery("lawsync_tasks", broker="redis://localhost:6379/0")

@celery_app.task(name="app.worker.morning_judicial_sync")
def morning_judicial_sync():
    db = SessionLocal()
    cases = db.query(Case).all()
    
    for case in cases:
        raw_text = ScraperFactory.get_data(case.state, case.suit_no)
        new_info = parse_court_data(raw_text)
        
        if new_info['status'] != case.last_status:
            pdf_filename = f"certs/Section84_{case.suit_no.replace('/', '_')}.pdf"
            create_pdf_certificate(new_info, output_path=pdf_filename)
            
            # 1. Informal Ping (Fast)
            send_telegram_alert(case.suit_no, new_info['status'])
            
            # 2. Formal Documentation (Permanent)
            send_formal_notification(
                suit_no=case.suit_no,
                recipient_email=case.lawyer_email,
                summary=new_info['status'],
                pdf_path=pdf_filename
            )
            
            case.last_status = new_info['status']
            db.commit()