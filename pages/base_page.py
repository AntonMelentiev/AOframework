from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:
    def __init__(self, _driver: WebDriver):
        self.driver = _driver

    @property
    def url(self):
        raise NotImplementedError

    def open(self):
        raise NotImplementedError
