from framework.page.element_container import ElementContainer
from framework.page.elements import TextInput
from framework.page.locators import CSS, CssType


class PageElements(ElementContainer):
    SEARCH_INPUT: TextInput = TextInput(locator=CSS(type=CssType.NAME, locator="q"))
