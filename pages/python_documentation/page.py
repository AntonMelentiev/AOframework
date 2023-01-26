import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from framework.page.page_base import PageBase
from pages.python_documentation.elements import PageElements


class PythonDocumentationPage(PageBase):
    _url = "https://docs.python.org/3/"
    _timeout = 15
    elements: PageElements = PageElements()

    @allure.step
    def open(self):
        self._driver.get(self._url)
        # TODO: move to base element
        WebDriverWait(self._driver, self._timeout).until(
            expected_conditions.visibility_of_element_located(
                (By.XPATH, "/html/body/div[2]/ul/li[9]/div/form/input[1]")
            )
        )

    @allure.step
    def search_text(self, text: str):
        self.elements.SEARCH_INPUT.fill(text)
        self.elements.SUBMIT_BUTTON.click()
        # TODO: move to base element
        # TODO: move to python_search page
        WebDriverWait(self._driver, self._timeout).until(
            expected_conditions.text_to_be_present_in_element(
                (By.XPATH, '//*[@id="search-results"]/h2'), "Search Results"
            )
        )
