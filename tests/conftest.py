import pytest
from playwright.sync_api import sync_playwright

from framework.constants import PROJECT_PATH
from framework.entry_point import T

pytest_plugins = [
    f"{__name__}_autouse",
]


@pytest.fixture
def browser(request):
    if str(request.fspath).startswith(str(PROJECT_PATH.joinpath("tests/ui"))):
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=False, slow_mo=50)

            yield browser

            browser.close()
    else:
        yield None


@pytest.fixture
def t(browser):
    t_object = T(browser=browser)

    yield t_object
