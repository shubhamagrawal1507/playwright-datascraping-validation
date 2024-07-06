from playwright.sync_api import sync_playwright
from playwright.sync_api import Page, expect
from src.utilities.data_loader import load_expected_data, save_scraped_data, load_scraped_data
from src.utilities.validations import validate_data
from pages.country_page import CountryPage


application_url = "https://cosmocode.io/automation-practice-webtable/"


def test_country_data_validation(page: Page):
    page.goto(application_url)
    country_page = CountryPage(page)    
    scraped_data = country_page.get_country_data()
    save_scraped_data(scraped_data, "data/scraped_data.csv")
    
    expected_data = load_expected_data("data/expected_data.csv")
    scraped_data_df = load_scraped_data("data/scraped_data.csv")
    
    validate_data(scraped_data_df, expected_data)
    
    page.close()
