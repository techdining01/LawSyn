from app.services.scrapers.lagos import scrape_lagos
from app.services.scrapers.abuja import scrape_abuja
from app.services.scrapers.oyo import scrape_oyo

class ScraperFactory:
    @staticmethod
    def get_data(state, suit_no):
        state = state.lower().strip()
        if "lagos" in state:
            return scrape_lagos(suit_no)
        elif "abuja" in state or "fct" in state:
            return scrape_abuja(suit_no)
        elif "oyo" in state:
            return scrape_oyo(suit_no)
        else:
            return f"Manual Search Required for {state}. Portal not yet integrated."