from framework.page.element_base import ElementBase


class Button(ElementBase):
    def click(self):
        self.el.click()


class TextInput(ElementBase):
    def fill(self, value: str) -> None:
        self.el.send_keys(value)

    @property
    def value(self) -> str:
        return self.el.get_attribute("value")


class Link(ElementBase):
    @property
    def url(self) -> str:
        return self.el.get_attribute("href")


class SpanWithText(ElementBase):
    @property
    def text(self) -> str:
        return self.el.get_inner_text()  # TODO: check if it's OK
