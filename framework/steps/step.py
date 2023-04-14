from playwright.sync_api import Browser

from framework.config import BASE_API_URL
from framework.steps.api import ApiStep
from framework.steps.page import PageStep


class Step:
    def __init__(self, browser: Browser = None):
        self.api = ApiStep(base_api_url=BASE_API_URL)

        if browser is not None:
            self.page = PageStep(browser=browser)
