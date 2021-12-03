import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import BasePage


class GooglePage(BasePage):
    url = "https://google.com"
    timeout = 15

    @property
    def _search_input(self):
        return self.driver.find_element_by_name("q")

    @property
    def _submit_button(self):
        return self.driver.find_element_by_name("btnK")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    @allure.step
    def open(self):
        self.driver.get(self.url)
        self.accept_policies()

    @allure.step
    def search_text(self, text: str):
        self._search_input.send_keys(text)
        self._submit_button.submit()

    @allure.step
    def get_text_after_search(self):
        return self.driver.find_element_by_name("q").get_attribute("value")

    def accept_policies(self):
        WebDriverWait(driver=self.driver, timeout=self.timeout).until(
            expected_conditions.visibility_of_element_located((By.ID, "L2AGLb"))
        )
        accept_btn = self.driver.find_element_by_id("L2AGLb")
        accept_btn.click()