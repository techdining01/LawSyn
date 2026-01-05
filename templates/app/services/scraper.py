from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

def scrape_lagos_case(suit_no):
    chrome_options = Options()
    chrome_options.add_argument("--headless") # Run in background
    driver = webdriver.Chrome(options=chrome_options)
    
    try:
        # The actual Lagos Judiciary URL (Simulation for this step)
        url = f"https://lagosjudiciary.gov.ng/case-status?suit={suit_no}"
        driver.get(url)
        time.sleep(3) # Wait for JS to load
        
        # We grab the main container where case info sits
        raw_text = driver.find_element(By.ID, "case-details").text
        return raw_text
    except Exception as e:
        return f"Scrape Error: {str(e)}"
    finally:
        driver.quit()

        