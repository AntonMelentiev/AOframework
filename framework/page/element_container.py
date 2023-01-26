from pydantic import BaseModel
from selenium.webdriver.remote.webdriver import WebDriver


class ElementContainer(BaseModel):
    def _set(self, driver: WebDriver):
        for el in self.__dict__.values():
            if isinstance(el, list):
                for sub_el in el:
                    sub_el._set(driver=driver)
            else:
                el._set(driver=driver)
