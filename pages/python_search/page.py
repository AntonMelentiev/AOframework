from typing import Union

import allure
from playwright.sync_api import Page

from framework.page.page_base import PageBase
from pages.python_search.elements import PageElements
from pages.python_search.elements import SearchResult


class PythonSearchPage(PageBase):
    _url = "https://docs.python.org/3/search.html"
    elements: PageElements = PageElements()

    def __init__(self, page: Page):
        super().__init__(page=page)
        self.elements.update_results(page=page)

    @allure.step
    def open(self):
        self._page.goto(self._url)
        self._page.wait_for_selector(f"{self.elements.SEARCH_RESULT_TITLE.selector} >> text=Search Results")
        self.elements.update_results(page=self._page)

    @allure.step
    def search_text(self, text: str) -> None:
        self.elements.SEARCH_INPUT.locator.fill(text)
        self.elements.SUBMIT_BUTTON.locator.click()
        self._page.wait_for_selector(self.elements.SEARCH_RESULT_TITLE.selector, state="visible")
        self.elements.update_results(page=self._page)

    @allure.step
    def get_first_search_result(self) -> Union[None, SearchResult]:
        if self.elements.SEARCH_RESULTS:
            return self.elements.SEARCH_RESULTS[0]

    @allure.step
    def get_number_of_results(self) -> int:
        return len(self.elements.SEARCH_RESULTS)
