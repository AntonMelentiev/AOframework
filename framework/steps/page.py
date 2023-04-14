from playwright.sync_api import Browser

from framework.utils.singletone import Singleton
from pages.google_results.page import GoogleResultsPage
from pages.google_search.page import GoogleSearchPage
from pages.python_documentation.page import PythonDocumentationPage
from pages.python_search.page import PythonSearchPage

pages = {
    "google_results": GoogleResultsPage,
    "google_search": GoogleSearchPage,
    "python_documentation": PythonDocumentationPage,
    "python_search": PythonSearchPage,
}


class PageStep(metaclass=Singleton):
    google_results: GoogleResultsPage
    google_search: GoogleSearchPage
    python_documentation: PythonDocumentationPage
    python_search: PythonSearchPage

    def __init__(self, browser: Browser):
        self._browser = browser
        self._page = self._browser.new_page()  # TODO: check if it's needed

        for page in pages:
            setattr(self.__class__, f"_{page}", None)
            self._set_page_getter(page)

    def _set_page_getter(self, name):
        setattr(self.__class__, name, property(fget=lambda self: self._get_page(name)))

    def _get_page(self, name):
        if getattr(self, f"_{name}") is None:
            setattr(self, f"_{name}", pages.get(name)(page=self._page))  # TODO: maybe new page should be sent

        return getattr(self, f"_{name}")
