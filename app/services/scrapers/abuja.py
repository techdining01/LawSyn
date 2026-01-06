from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def scrape_abuja(suit_no):
    options = Options()
    options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)
    
    try:
        # FCT High Court Case Tracking URL
        driver.get("https://fcthighcourt.gov.ng/case-tracking/") 
        
        # 1. Wait for the search input
        search_field = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.ID, "search_suit_no"))
        )
        search_field.send_keys(suit_no)
        
        # 2. Click Search
        search_button = driver.find_element(By.ID, "btn_search")
        search_button.click()
        
        # 3. Capture the result table
        # Abuja usually returns a row with Suit No, Parties, and Status
        result_table = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.CLASS_NAME, "table-responsive"))
        )
        return result_table.text
    except Exception as e:
        return f"ABUJA_PORTAL_ERROR: {str(e)}"
    finally:
        driver.quit()