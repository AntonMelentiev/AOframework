import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import BasePage


class GooglePage(BasePage):
    _url = "https://google.com"
    _timeout = 15

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    @property
    def _search_input(self):
        return self._driver.find_element_by_name("q")

    @property
    def _submit_button(self):
        return self._driver.find_element_by_name("btnK")

    def _accept_policies(self):
        accept_btn = WebDriverWait(self._driver, self._timeout).until(
            expected_conditions.visibility_of_element_located((By.ID, "L2AGLb"))
        )
        accept_btn.click()

    ####################################################################################################################
    # Actions
    ####################################################################################################################

    @allure.step
    def open(self):
        self._driver.get(self._url)
        self._accept_policies()

    @allure.step
    def search_text(self, text: str):
        self._search_input.send_keys(text)
        self._submit_button.submit()

    @allure.step
    def get_text_after_search(self):
        return self._driver.find_element_by_name("q").get_attribute("value")
