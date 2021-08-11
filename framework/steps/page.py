from selenium.webdriver.remote.webdriver import WebDriver

from pages.google_page import GooglePage


class Page:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self._google = None

    @property
    def google(self):
        if self._google is None:
            self._google = GooglePage(driver=self.driver)

        return self._google
