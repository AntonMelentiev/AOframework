from selenium import webdriver

from framework.base_test.test_data_creator import TestDataCreator
from framework.base_test.check import Check
from framework.base_test.page import Page


class Step:
    def __init__(self, driver: webdriver):
        self.page = Page(driver=driver)
        self.check = Check()


class T:
    def __init__(self, driver: webdriver):
        self.step = Step(driver=driver)
        self.data = TestDataCreator()
