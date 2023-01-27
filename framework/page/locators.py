from dataclasses import dataclass


class CssType:
    NAME = "name"
    NAME_WITH_NON_ZERO_SIZE = "name_with_non_zero_size"
    CSS_SELECTOR = "css_selector"


@dataclass
class Locator:
    locator: str


@dataclass
class CSS(Locator):
    type: CssType


class XPATH(Locator):
    ...
