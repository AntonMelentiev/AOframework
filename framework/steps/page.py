from selenium.webdriver.remote.webdriver import WebDriver

from pages.google_page import GooglePage
from pages.python_page import PythonPage


class Page:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self._google = None
        self._python = None

    @property
    def google(self):
        if self._google is None:
            self._google = GooglePage(driver=self.driver)

        return self._google

    @property
    def python(self):
        if self._python is None:
            self._python = PythonPage(driver=self.driver)

        return self._python
