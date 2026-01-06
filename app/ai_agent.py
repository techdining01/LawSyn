from google import genai
from dotenv import load_dotenv
from google import genai
import os, json

load_dotenv()


# The new "Boss" object
client = genai.Client(api_key=os.getenv("GEMINI_KEY"))


def parse_court_data(raw_text):
    prompt = f"""
   Extract data from this raw scrape for a Section 84 Certificate.
    Raw Data: {raw_text}
    
    Return ONLY JSON with these exact keys:
    "claimant", "defendant", "suit_no", "last_hearing", "status", "division"
    """
    
    response = client.models.generate_content(
        model='gemini-2.0-flash',
        contents=prompt
    )
    print(response)
    # Clean the response in case of markdown formatting
    clean_json = response.text.replace("```json", "").replace("```", "").strip()
    return json.loads(clean_json)

