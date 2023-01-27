from framework.page.element_container import ElementContainer
from framework.page.elements import Button, TextInput
from framework.page.locators import CSS, CssType


class PageElements(ElementContainer):
    SEARCH_INPUT: TextInput = TextInput(locator=CSS(type=CssType.NAME, locator="q"))
    SUBMIT_BUTTON: Button = Button(locator=CSS(type=CssType.NAME_WITH_NON_ZERO_SIZE, locator="btnK"))
