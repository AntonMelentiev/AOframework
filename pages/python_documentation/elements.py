from framework.page.page_element import PageElement
from framework.page.page_elements_container import ElementContainer


class PageElements(ElementContainer):
    SEARCH_INPUT: PageElement = PageElement(selector="//html/body/div[2]/ul/li[9]/div/form/input[1]")
    SUBMIT_BUTTON: PageElement = PageElement(selector="//html/body/div[2]/ul/li[9]/div/form/input[2]")
    SEARCH_RESULT_TITLE: PageElement = PageElement(selector="//*[@id='search-results']/h2")
