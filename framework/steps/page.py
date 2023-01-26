from selenium.webdriver.remote.webdriver import WebDriver

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


class Page:
    google_results: GoogleResultsPage
    google_search: GoogleSearchPage
    python_documentation: PythonDocumentationPage
    python_search: PythonSearchPage

    def __init__(self, driver: WebDriver):
        self._driver = driver

        for page in pages:
            setattr(self.__class__, f"_{page}", None)
            self._set_page_getter(page)

    def _set_page_getter(self, name):
        setattr(self.__class__, name, property(fget=lambda self: self._get_page(name)))

    def _get_page(self, name):
        if getattr(self, f"_{name}") is None:
            setattr(self, f"_{name}", pages.get(name)(driver=self._driver))

        return getattr(self, f"_{name}")
