from framework.page.element_base import ElementBase


class Button(ElementBase):
    def click(self):
        self._element.click()


class TextInput(ElementBase):
    def fill(self, value: str) -> None:
        self._element.send_keys(value)

    @property
    def value(self) -> str:
        return self._element.get_attribute("value")


class Link(ElementBase):
    @property
    def url(self) -> str:
        return self._element.get_attribute("href")


class SpanWithText(ElementBase):
    @property
    def text(self) -> str:
        return self._element.get_inner_text()  # TODO: check if it's OK
