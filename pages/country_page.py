from playwright.sync_api import Page

class CountryPage:

    def __init__(self, page: Page):
        self.page = page

    def get_country_data(self):
        countries = self.page.locator("//table//tr")
        data = []
        index = 1
        while index < countries.count():
            countries.nth(index).scroll_into_view_if_needed()
            country_name = countries.nth(index).locator("//td[2]").inner_text()
            capital = countries.nth(index).locator("//td[3]").inner_text()
            currency = countries.nth(index).locator("//td[4]").inner_text()
            language = countries.nth(index).locator("//td[5]").inner_text()
            data.append({"Country": country_name, "Capital(s)": capital, "Currency": currency,"Primary Language(s)":language})
            index = index + 1
        return data
