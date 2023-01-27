from typing import Optional, Union

from pydantic import BaseModel
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement

from framework.page.locators import CSS, XPATH, CssType, Locator


class ElementBase(BaseModel):
    locator: Locator
    driver: Optional[WebDriver] = None

    class Config:
        arbitrary_types_allowed = True

    @property
    def _css_map(self):
        def get_by_name_with_non_zero_size(name: str) -> Union[None, WebElement]:
            els = self.driver.find_elements_by_name(name=name)
            for el in els:
                if el.size["width"] > 0 and el.size["height"] > 0:
                    return el

        return {
            CssType.NAME: self.driver.find_element_by_name,
            CssType.NAME_WITH_NON_ZERO_SIZE: get_by_name_with_non_zero_size,
            CssType.CSS_SELECTOR: self.driver.find_element_by_css_selector,
        }

    def _set(self, driver: WebDriver):
        self.driver = driver

    @property
    def el(self) -> WebElement:
        if isinstance(self.locator, CSS):
            return self._css_map[self.locator.type](self.locator.locator)
        elif isinstance(self.locator, XPATH):
            return self.driver.find_element_by_xpath(self.locator.locator)
