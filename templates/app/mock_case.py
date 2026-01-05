from app.worker import sync_and_alert_task

# This triggers the full loop: Scrape -> AI Analysis -> Lawyer Alert
# Using your email for the test
sync_and_alert_task.delay("kwara", "KWS/22/2025", "your_email@example.com")