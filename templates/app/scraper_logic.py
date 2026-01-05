from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# def selenium_search_lagos(suit_number):
#     # Setup 'Headless' mode so a window doesn't pop up on your server
#     chrome_options = Options()
#     chrome_options.add_argument("--headless")
    
#     driver = webdriver.Chrome(options=chrome_options)
    
#     try:
#         driver.get("https://lagosjudiciary.gov.ng/search.aspx")
#         # Selenium physically finds the search box and types
#         search_box = driver.find_element(By.ID, "txtSuitNo")
#         search_box.send_keys(suit_number)
        
#         search_button = driver.find_element(By.ID, "btnSearch")
#         search_button.click()
        
#         # Grab the result
#         result = driver.find_element(By.CLASS_NAME, "case-status").text
#         return result
#     finally:
#         driver.quit() # Always close the browser!



from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

def get_driver():
    options = Options()
    options.add_argument("--headless") # Runs in background
    options.add_argument("--no-sandbox")
    return webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

def scrape_court_status(state_id, suit_no):
    driver = get_driver()
    try:
        if state_id == "lagos":
            # Target: Lagos JIS Search
            driver.get("https://lagosjudiciary.gov.ng/search.aspx")
            # Logic: Find input, type suit no, click search
            driver.find_element(By.ID, "txtSuitNo").send_keys(suit_no)
            driver.find_element(By.ID, "btnSearch").click()
            # Grab the text from the status column
            result = driver.find_element(By.CLASS_NAME, "case-status").text
            return result

        elif state_id == "abuja":
            # Target: FCT High Court Cause List
            driver.get("https://www.fcthighcourt.gov.ng/cause-list/")
            # Logic: Abuja lists cases in a table. We search for the suit no in the table text.
            page_content = driver.find_element(By.TAG_NAME, "body").text
            if suit_no in page_content:
                return "Listed on current Cause List"
            return "Not found on today's list"

        # Expand for other 13 states here...
        
    except Exception as e:
        return f"Error: {str(e)}"
    finally:
        driver.quit()


# def scrape_court_status(state_id, suit_no):
#     # For now, we return a success string. 
#     # Later, we insert the Selenium code here.
#     return f"Case {suit_no} in {state_id} is adjourned to March 2026."

def save_to_database(state, suit_no, status, ai_insight):
    # This simulates saving to a database
    print(f"--- SAVED TO DB: {suit_no} in {state} ---")
    print(f"Status: {status}")
    print(f"AI Insight: {ai_insight[:50]}...")


