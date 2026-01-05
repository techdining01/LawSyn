
from google import genai
import os
from dotenv import load_dotenv

load_dotenv()


# The new "Boss" object
client = genai.Client(api_key=os.getenv("GEMINI_KEY"))

async def analyze_case_status(scraped_text, state_name):
    # Notice the new syntax: client.models.generate_content
    response = client.models.generate_content(
        model='gemini-2.0-flash', # Using the latest 2026 model
        contents=f"Summarize this {state_name} court status for a lawyer: {scraped_text}"
    )
    return response.text



def generate_legal_alert(state, raw_data):
    """
    Uses the upgraded 2.0 Flash model to analyze court data.
    """
    try:
        # Notice the new 'models.generate_content' syntax
        response = client.models.generate_content(
            model='gemini-2.0-flash', 
            contents=f"Summarize this {state} court status for a lawyer: {raw_data}"
        )
        return response.text
    except Exception as e:
        return f"AI Error: {str(e)}"
    


def extract_case_details(raw_scrape):
    prompt = f"""
    Analyze this raw Nigerian court data and return ONLY a JSON object:
    Raw Data: {raw_scrape}
    Required Keys: "claimant", "defendant", "last_event", "is_small_claims"
    """
    
    response = client.models.generate_content(
        model='gemini-2.0-flash',
        contents=prompt
    )
    # This turns the raw scrape into the structured data for your PDF
    return response.text



