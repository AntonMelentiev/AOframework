import allure

from framework.page.page_base import PageBase
from pages.google_search.elements import PageElements


class GoogleSearchPage(PageBase):
    _url = "https://google.com"
    elements: PageElements = PageElements()

    def _accept_policies(self):
        self._page.wait_for_selector(self.elements.ACCEPT_POLICIES_BUTTON.selector, state="attached")
        self.elements.ACCEPT_POLICIES_BUTTON.locator.click()

    @allure.step
    def open(self):
        self._page.goto(self._url)
        self._accept_policies()

    @allure.step
    def search_text(self, text: str):
        self._page.wait_for_timeout(timeout=250)
        # self._page.wait_for_selector(self.elements.SEARCH_INPUT.selector, state="attached", timeout=3000)
        self.elements.SEARCH_INPUT.locator.fill(text)
        self.elements.SUBMIT_BUTTON.locator.all()[0].click(timeout=1000)

    @allure.step
    def get_text_after_search(self):
        return self.elements.SEARCH_INPUT.locator.input_value()
