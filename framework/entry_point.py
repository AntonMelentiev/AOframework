from playwright.sync_api import Browser

from framework.data.test_data_creator import TestDataCreator
from framework.steps.check import Check
from framework.steps.step import Step


class T:
    def __init__(self, browser: Browser = None):
        self.data = TestDataCreator()
        self.step = Step(browser=browser)
        self.check = Check()
