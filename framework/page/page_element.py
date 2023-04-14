from typing import Optional, TYPE_CHECKING

from playwright.sync_api import Locator, Page
from pydantic import BaseModel


class PageElement(BaseModel):
    selector: str
    page: Optional[Page] = None

    class Config:
        arbitrary_types_allowed = True

    def __getattr__(self, item):
        if (item in dir(BaseModel)) and (item in dir(Locator)):
            raise AttributeError(f"'{self.__class__.__name__}' object has duplicated attribute '{item}'. Fix it!!!")
        if item in dir(Locator):
            return getattr(self.locator, item)
        raise AttributeError(f"'{self.__class__.__name__}' object has not attribute '{item}'")

    def _set(self, page: Page):
        self.page = page

    @property
    def locator(self) -> Locator:
        return self.page.locator(self.selector)


# Help for PyCharm
if TYPE_CHECKING:
    class PageElement(BaseModel, Locator):
        def __init__(self, selector: str, page: Optional[Page]):
            ...
