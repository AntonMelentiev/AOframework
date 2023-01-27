from selenium.webdriver.remote.webdriver import WebDriver

from framework.page.element_container import ElementContainer
from framework.page.waiter import Waiter


class PageBase:
    def __init__(self, driver: WebDriver):
        self._driver = driver
        self._wait = Waiter(driver=self._driver)

        self.elements._set(driver=self._driver)

    @property
    def _url(self) -> str:
        raise NotImplementedError

    @property
    def elements(self) -> ElementContainer:
        raise NotImplementedError

    def open(self) -> None:
        self._driver.get(self._url)
