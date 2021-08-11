from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    @property
    def url(self):
        raise NotImplementedError

    def open(self):
        raise NotImplementedError
