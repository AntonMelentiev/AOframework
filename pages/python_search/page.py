from typing import Union

import allure
from selenium.webdriver.remote.webdriver import WebDriver

from framework.page.locators import XPATH
from framework.page.page_base import PageBase
from pages.python_search.elements import PageElements
from pages.python_search.elements import SearchResult


class PythonSearchPage(PageBase):
    _url = "https://docs.python.org/3/search.html"
    _timeout = 15
    elements: PageElements = PageElements()

    def __init__(self, driver: WebDriver):
        super().__init__(driver=driver)
        self.elements.update_results(driver=driver)

    @allure.step
    def open(self):
        self._driver.get(self._url)
        self._wait.text_to_be_present_in_element(
            locator=XPATH(locator="//*[@id='search-results']/h2"), text="Search Results"
        )
        self.elements.update_results(driver=self._driver)

    @allure.step
    def search_text(self, text: str) -> None:
        self.elements.SEARCH_INPUT.fill(text)
        self.elements.SUBMIT_BUTTON.click()
        self._wait.text_to_be_present_in_element(
            locator=XPATH(locator="//*[@id='search-results']/h2"), text="Search Results"
        )
        self.elements.update_results(driver=self._driver)

    @allure.step
    def get_first_search_result(self) -> Union[None, SearchResult]:
        if self.elements.SEARCH_RESULTS:
            return self.elements.SEARCH_RESULTS[0]

    @allure.step
    def get_number_of_results(self) -> int:
        return len(self.elements.SEARCH_RESULTS)
