from selenium.webdriver.remote.webdriver import WebDriver

from pages.google_page import GooglePage
from pages.python_page import PythonPage


pages = {
    "google": GooglePage,
    "python": PythonPage,
}


class Page:
    google: GooglePage
    python: PythonPage

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
