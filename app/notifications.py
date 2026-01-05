import smtplib
from email.message import EmailMessage

def send_invasive_alert(lawyer_email, case_details, ai_insight):
    msg = EmailMessage()
    msg.set_content(f"""
    URGENT LAWSYNC UPDATE:
    
    Case: {case_details['suit_no']} ({case_details['state']})
    New Status: {case_details['status']}
    
    AI ANALYSIS:
    {ai_insight}
    
    Please log in to LawSync to generate your Section 84 Certificate.
    """)
    
    msg['Subject'] = f"ALERT: Change in {case_details['state']} Court Schedule"
    msg['From'] = "alerts@lawsync.ng"
    msg['To'] = lawyer_email

    # Logic to send via SMTP (e.g. Gmail/SendGrid)
    # with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    #     smtp.login(EMAIL_USER, EMAIL_PASS)
    #     smtp.send_message(msg)
    print(f"Invasive alert pushed to {lawyer_email}")



def send_invasive_alert(email, case_data, insight):
    # This simulates the email/WhatsApp push
    print(f"--- NOTIFICATION SENT TO {email} ---")
    print(f"Subject: Update on {case_data['suit_no']}")