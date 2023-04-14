from framework.page.page_element import PageElement
from framework.page.page_elements_container import ElementContainer


class PageElements(ElementContainer):
    SEARCH_INPUT: PageElement = PageElement(selector='textarea[name="q"]')
    SUBMIT_BUTTON: PageElement = PageElement(selector='input[name="btnK"]')
    ACCEPT_POLICIES_BUTTON: PageElement = PageElement(selector="#L2AGLb")
