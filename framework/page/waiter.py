from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from framework.page.locators import Locator, XPATH, CSS


class Waiter:
    def __init__(self, driver: WebDriver):
        self._driver = driver
        self._timeout = 10
        self.locator_map = {
            XPATH: By.XPATH,
            CSS: By.CSS_SELECTOR,
        }

    def text_to_be_present_in_element(self, locator: Locator, text: str, timeout: int = None) -> None:
        WebDriverWait(driver=self._driver, timeout=timeout or self._timeout).until(
            expected_conditions.text_to_be_present_in_element(
                locator=(self.locator_map.get(type(locator)), locator.locator), text_=text
            )
        )

    def visibility_of_element_located(self, locator: Locator, timeout: int = None) -> None:
        WebDriverWait(driver=self._driver, timeout=timeout or self._timeout).until(
            expected_conditions.visibility_of_element_located(
                locator=(self.locator_map.get(type(locator)), locator.locator)
            )
        )
