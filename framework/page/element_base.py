from typing import Optional

from pydantic import BaseModel
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement

from framework.page.locators import CSS, XPATH, CssType, Locator


class ElementBase(BaseModel):
    locator: Optional[Locator] = None
    driver: Optional[WebDriver] = None
    el: Optional[WebElement] = None

    class Config:
        arbitrary_types_allowed = True

    @property
    def _css_map(self):
        return {
            CssType.NAME: self.driver.find_element_by_name
        }

    def _set(self, driver: WebDriver):
        self.driver = driver

    def _get_self(self) -> None:
        if isinstance(self.locator, CSS):
            self.el = self._css_map[self.locator.type](self.locator.locator)
        elif isinstance(self.locator, XPATH):
            self.el = self.driver.find_element_by_xpath(self.locator.locator)

    @property
    def _element(self) -> WebElement:
        if self.el is None:
            self._get_self()

        return self.el
