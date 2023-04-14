from playwright.sync_api import Page
from pydantic import BaseModel


class ElementContainer(BaseModel):
    def _set(self, page: Page):
        for el in self.__dict__.values():
            if isinstance(el, list):
                for sub_el in el:
                    sub_el._set(page=page)
            else:
                el._set(page=page)
