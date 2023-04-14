import allure

from framework.page.page_base import PageBase
from pages.google_results.elements import PageElements


class GoogleResultsPage(PageBase):
    _url = "https://www.google.com/search?q=results"
    elements: PageElements = PageElements()

    @allure.step
    def get_text_after_search(self) -> str:
        return self.elements.SEARCH_INPUT.input_value()
