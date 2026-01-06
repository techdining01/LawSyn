import os
import requests
import datetime
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

def send_formal_notification(suit_no, recipient_email, summary, pdf_path=None):
    # --- 1. SEND GMAIL (FORMAL) ---
    sender = os.getenv("GMAIL_USER")
    password = os.getenv("GMAIL_APP_PASSWORD")
    
    msg = MIMEMultipart()
    msg['From'] = f"LawSync Sentinel <{sender}>"
    msg['To'] = recipient_email
    msg['Subject'] = f"FORMAL NOTICE: Status Update for Case {suit_no}"

    body = f"""
    Dear Counsel,

    This is a formal automated notification regarding Case No: {suit_no}.
    
    COURT STATUS UPDATE: 
    {summary}

    Attached to this email is the generated Section 84 Certificate for your records. 
    This document has been formatted for immediate judicial filing.

    Regards,
    LawSync Pro Engine
    """
    msg.attach(MIMEText(body, 'plain'))

    # Attach PDF
    if pdf_path and os.path.exists(pdf_path):
        with open(pdf_path, "rb") as attachment:
            part = MIMEBase("application", "octet-stream")
            part.set_payload(attachment.read())
            encoders.encode_base64(part)
            part.add_header("Content-Disposition", f"attachment; filename=Section84_{suit_no.replace('/', '_')}.pdf")
            msg.attach(part)

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(sender, password)
            server.send_message(msg)
            print("✅ Formal Email Sent.")
    except Exception as e:
        print(f"❌ Gmail Error: {e}")



TELEGRAM_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

def send_telegram_alert(suit_no, summary, pdf_path=None):
    """Sends a text summary and the Section 84 PDF to the lawyer."""
    # 1. Send Text Alert
    text_url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": f"🚨 *LAWSYNC ALERT*\n\n*Suit:* {suit_no}\n*Update:* {summary}\n_Your Section 84 Cert is attached._",
        "parse_mode": "Markdown"
    }
    requests.post(text_url, data=payload)

    # 2. Send PDF Document
    if pdf_path and os.path.exists(pdf_path):
        doc_url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendDocument"
        with open(pdf_path, 'rb') as doc:
            files = {'document': doc}
            requests.post(doc_url, data={'chat_id': CHAT_ID}, files=files)