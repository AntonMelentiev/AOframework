from typing import Optional

from pydantic import BaseModel
from selenium.webdriver.remote.webdriver import WebDriver

from framework.page.waiter import Waiter


class ElementContainer(BaseModel):
    wait: Optional[Waiter] = None

    class Config:
        arbitrary_types_allowed = True

    def _set(self, driver: WebDriver):
        self.wait = Waiter(driver=driver)

        for el in self.__dict__.values():
            if isinstance(el, Waiter):
                continue
            if isinstance(el, list):
                for sub_el in el:
                    sub_el._set(driver=driver)
            else:
                el._set(driver=driver)
