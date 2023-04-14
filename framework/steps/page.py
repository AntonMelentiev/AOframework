from playwright.sync_api import Browser

from framework.utils.singletone import Singleton
from pages.google_results.page import GoogleResultsPage
from pages.google_search.page import GoogleSearchPage
from pages.python_documentation.page import PythonDocumentationPage
from pages.python_search.page import PythonSearchPage


class PageStep(metaclass=Singleton):
    google_results: GoogleResultsPage
    google_search: GoogleSearchPage
    python_documentation: PythonDocumentationPage
    python_search: PythonSearchPage

    def __init__(self, browser: Browser):
        self._browser = browser
        self._page = self._browser.new_page()  # TODO: check if it's needed

        for page_name, page_type in self.__annotations__.items():
            setattr(self.__class__, f"_{page_name}", None)
            self._set_page_getter(page_name, page_type)

    def _set_page_getter(self, page_name, page_type):
        setattr(self.__class__, page_name, property(fget=lambda self: self._get_page(page_name, page_type)))

    def _get_page(self, page_name, page_type):
        if getattr(self, f"_{page_name}") is None:
            setattr(self, f"_{page_name}", page_type(page=self._page))  # TODO: maybe new page should be sent

        return getattr(self, f"_{page_name}")
