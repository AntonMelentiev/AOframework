from typing import Union

from selenium.webdriver.remote.webdriver import WebDriver

from framework.config import BASE_API_URL
from framework.steps.api import ApiStep
from framework.steps.check import Check
from framework.steps.page import Page


class Step:
    def __init__(self, driver: Union[WebDriver, None]):
        self.api = ApiStep(base_api_url=BASE_API_URL)
        self.check = Check()

        if driver is not None:
            self.page = Page(driver=driver)
