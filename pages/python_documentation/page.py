import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from framework.page.locators import XPATH
from framework.page.page_base import PageBase
from pages.python_documentation.elements import PageElements


class PythonDocumentationPage(PageBase):
    _url = "https://docs.python.org/3/"
    _timeout = 15
    elements: PageElements = PageElements()

    @allure.step
    def open(self):
        self._driver.get(self._url)
        self.elements.wait.visibility_of_element_located(
            locator=XPATH(locator="html/body/div[2]/ul/li[9]/div/form/input[1]")
        )

    @allure.step
    def search_text(self, text: str):
        self.elements.SEARCH_INPUT.fill(text)
        self.elements.SUBMIT_BUTTON.click()
        self.elements.wait.text_to_be_present_in_element(
            locator=XPATH(locator="//*[@id='search-results']/h2"),
            text="Search Results",
            timeout=15,
        )
