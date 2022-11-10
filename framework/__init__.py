from typing import Union

from selenium.webdriver.remote.webdriver import WebDriver

from framework.data.test_data_creator import TestDataCreator
from framework.steps import Step


class T:
    def __init__(self, driver: Union[WebDriver, None]):
        self.step = Step(driver=driver)
        self.data = TestDataCreator()
