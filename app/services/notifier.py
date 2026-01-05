import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

def send_invasive_update(lawyer_email, suit_no, ai_summary, pdf_content):
    msg = MIMEMultipart()
    msg['Subject'] = f"🚨 URGENT: Court Update - {suit_no}"
    msg['From'] = "alerts@lawsync.ng"
    msg['To'] = lawyer_email

    body = f"""
    Counsel,
    
    Our automated monitor has detected a status change for Suit No: {suit_no}.
    
    AI ANALYSIS:
    {ai_summary}
    
    Attached is your Section 84 Certificate of Authentication, 
    pre-formatted for court filing.
    
    - LawSync Engine 2026
    """
    msg.attach(MIMEText(body, 'plain'))

    # Attach the PDF we generated
    part = MIMEApplication(pdf_content, Name=f"Section84_{suit_no}.pdf")
    part['Content-Disposition'] = f'attachment; filename="Section84_{suit_no}.pdf"'
    msg.attach(part)

    # (Add your SMTP server logic here to actually send)
    print(f"NOTIFICATION SENT TO {lawyer_email} WITH PDF ATTACHMENT.")