from framework.page.element_container import ElementContainer
from framework.page.elements import Button, TextInput
from framework.page.locators import CSS, CssType, XPATH


class PageElements(ElementContainer):
    SEARCH_INPUT: TextInput = TextInput(locator=XPATH(locator="/html/body/div[2]/ul/li[9]/div/form/input[1]"))
    SUBMIT_BUTTON: Button = Button(locator=XPATH(locator="/html/body/div[2]/ul/li[9]/div/form/input[2]"))
