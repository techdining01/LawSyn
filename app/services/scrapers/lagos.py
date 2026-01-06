from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def scrape_lagos(suit_no):
    options = Options()
    options.add_argument("--headless") 
    options.add_argument("--no-sandbox")
    driver = webdriver.Chrome(options=options)
    
    try:
        # Direct URL to the Lagos Case Search
        driver.get("https://lagosjudiciary.gov.ng/case-status")
        
        # 1. Target the search input and fire the suit number
        search_box = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "suit_no"))
        )
        search_box.send_keys(suit_no)
        search_box.submit()
        
        # 2. Extract the result container
        result_area = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "case-details-table"))
        )
        return result_area.text # This is the raw "Truth" from the court
    except Exception as e:
        return f"CRITICAL_ERROR: {str(e)}"
    finally:
        driver.quit()