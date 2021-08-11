from selenium import webdriver

from framework.steps.check import Check
from framework.steps.page import Page


class Step:
    def __init__(self, driver: webdriver):
        self.page = Page(driver=driver)
        self.check = Check()
