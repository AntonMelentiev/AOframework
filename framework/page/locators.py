from dataclasses import dataclass


class CssType:
    NAME = "name"


@dataclass
class Locator:
    locator: str


@dataclass
class CSS(Locator):
    type: CssType


class XPATH(Locator):
    ...
