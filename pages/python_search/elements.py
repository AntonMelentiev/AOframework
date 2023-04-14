from typing import List

from playwright.sync_api import Page

from framework.page.page_element import PageElement
from framework.page.page_elements_container import ElementContainer


class SearchResult(ElementContainer):
    LINK: PageElement
    TEXT: PageElement


class PageElements(ElementContainer):
    SEARCH_INPUT: PageElement = PageElement(selector='[name="q"]')
    SEARCH_RESULT_TITLE: PageElement = PageElement(selector="//*[@id='search-results']/h2")
    SEARCH_RESULTS: List[SearchResult] = []
    SUBMIT_BUTTON: PageElement = PageElement(selector="/html/body/div[2]/ul/li[9]/div/form/input[2]")

    def update_results(self, page: Page):
        results_list = page.locator(selector=".search")
        results = results_list.locator("li").all()

        self.SEARCH_RESULTS = []
        for i in range(1, len(results) + 1):
            obj = SearchResult(
                LINK=PageElement(selector=f"//li[a and span or p][{i}]/a"),
                TEXT=PageElement(selector=f"//li[a and span or p][{i}]/*[2]"),
            )
            obj._set(page=page)
            self.SEARCH_RESULTS.append(obj)
