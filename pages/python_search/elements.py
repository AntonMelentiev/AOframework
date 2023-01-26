from typing import List

from selenium.webdriver.remote.webdriver import WebDriver

from framework.page.element_container import ElementContainer
from framework.page.elements import Button, TextInput, Link, SpanWithText
from framework.page.locators import CSS, CssType, XPATH


class SearchResult(ElementContainer):
    LINK: Link
    TEXT: SpanWithText


class PageElements(ElementContainer):
    SEARCH_INPUT: TextInput = TextInput(locator=CSS(type=CssType.NAME, locator="q"))
    SEARCH_RESULTS: List[SearchResult] = []
    SUBMIT_BUTTON: Button = Button(locator=XPATH(locator="/html/body/div[3]/div[1]/div/div/form/input[2]"))

    def update_results(self, driver: WebDriver):
        results_list = driver.find_element_by_class_name("search")
        results = results_list.find_elements_by_tag_name("li")

        self.SEARCH_RESULTS = []
        for i in range(1, len(results) + 1):
            obj = SearchResult(
                LINK=Link(locator=XPATH(locator=f"//li[a and span][{i}]/a")),
                TEXT=SpanWithText(locator=XPATH(locator=f"//li[a and span][{i}]/span")),
            )
            obj._set(driver=driver)
            self.SEARCH_RESULTS.append(obj)
