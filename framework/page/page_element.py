from typing import Optional

from playwright.sync_api import Locator, Page
from pydantic import BaseModel


class PageElement(BaseModel):
    selector: str
    page: Optional[Page] = None

    class Config:
        arbitrary_types_allowed = True

    def _set(self, page: Page):
        self.page = page

    @property
    def locator(self) -> Locator:
        return self.page.locator(self.selector)
