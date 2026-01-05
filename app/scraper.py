import requests
from bs4 import BeautifulSoup

def scrape_lagos_case(suit_number):
    url = f"https://lagosjudiciary.gov.ng/search.aspx?q={suit_number}"
    
    try:
        response = requests.get(url, timeout=10)
        soup = BeautifulSoup(response.content, "html.parser")
        
        # We look for the 'Case Status' table in the Lagos JIS
        case_table = soup.find("table", {"id": "caseStatusTable"})
        
        if case_table:
            # Extract the 2nd row (usually the latest status)
            latest_update = case_table.find_all("tr")[1].text.strip()
            return {"status": "Success", "data": latest_update}
        else:
            return {"status": "Not Found", "data": "No record for this Suit Number."}
            
    except Exception as e:
        return {"status": "Error", "error": str(e)}
    
    