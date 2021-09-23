from selenium import webdriver

from framework.base_test.TestDataCreator import TestDataCreator
from framework.base_test.check import Check
from framework.base_test.page import Page


class Test:
    def __init__(self, driver: webdriver):
        self.page = Page(driver=driver)
        self.test_data = TestDataCreator()
        self.check = Check()
