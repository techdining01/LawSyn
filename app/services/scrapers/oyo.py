from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def scrape_oyo(suit_no):
    options = Options()
    options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)
    try:
        driver.get("https://comis.oyostatejudiciary.oy.gov.ng/")
        # Find search bar for suit number
        search_box = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='text']"))
        )
        search_box.send_keys(suit_no)
        search_box.submit()
        
        # Extract case summary table
        details = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "table"))
        )
        return details.text
    except Exception as e:
        return f"OYO_PORTAL_ERROR: {str(e)}"
    finally:
        driver.quit()