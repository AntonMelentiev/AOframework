from playwright.sync_api import Page

from framework.page.page_elements_container import ElementContainer


class PageBase:
    def __init__(self, page: Page):
        self._page = page
        # set elements
        self.elements._set(page=self._page)

    @property
    def _url(self) -> str:
        raise NotImplementedError

    @property
    def elements(self) -> ElementContainer:
        raise NotImplementedError

    def open(self) -> None:
        self._page.goto(self._url)
