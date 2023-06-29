import allure

from framework.page.page_base import PageBase
from pages.python_documentation.elements import PageElements


class PythonDocumentationPage(PageBase):
    _url = "https://docs.python.org/3/"
    elements: PageElements = PageElements()

    @allure.step
    def open(self):
        self._page.goto(self._url)
        self._page.wait_for_selector(self.elements.SEARCH_INPUT.selector, state="visible")

    @allure.step
    def search_text(self, text: str):
        self.elements.SEARCH_INPUT.fill(text)
        self.elements.SUBMIT_BUTTON.click()
        self._page.wait_for_selector(f"{self.elements.SEARCH_RESULT_TITLE.selector} >> text=Search Results")
