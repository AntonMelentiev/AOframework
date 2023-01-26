from selenium.webdriver.remote.webdriver import WebDriver

from framework.page.element_container import ElementContainer


class PageBase:
    def __init__(self, driver: WebDriver):
        self._driver = driver
        self.elements._set(driver=self._driver)

    @property
    def _url(self) -> str:
        raise NotImplementedError

    @property
    def elements(self) -> ElementContainer:
        raise NotImplementedError

    def open(self) -> None:
        self._driver.get(self._url)
