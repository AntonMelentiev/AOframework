import allure
from selenium.webdriver.common.by import By

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from framework.page.page_base import PageBase
from pages.google_search.elements import PageElements


class GoogleSearchPage(PageBase):
    _url = "https://google.com"
    _timeout = 15
    elements: PageElements = PageElements()

    def _accept_policies(self):
        accept_btn = WebDriverWait(self._driver, self._timeout).until(
            expected_conditions.visibility_of_element_located((By.ID, "L2AGLb"))
        )
        accept_btn.click()

    @allure.step
    def open(self):
        self._driver.get(self._url)
        self._accept_policies()

    @allure.step
    def search_text(self, text: str):
        self.elements.SEARCH_INPUT.fill(text)
        self.elements.SUBMIT_BUTTON.click()

    @allure.step
    def get_text_after_search(self):
        return self._driver.find_element_by_name("q").get_attribute("value")
