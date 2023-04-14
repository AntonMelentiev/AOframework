import allure
import pytest
from playwright.sync_api import sync_playwright

from framework.constants import PROJECT_PATH
from framework.entry_point import T
from framework.utils.allure_helpers import get_screenshot_name


# See http://doc.pytest.org/en/latest/example/simple.html#making-test-result-information-available-in-fixtures
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):  # pylint: disable=unused-argument
    # Execute all other hooks to obtain the report object
    outcome = yield
    rep = outcome.get_result()

    # Set a report attribute for each phase of a call, which can be "setup", "call", "teardown"
    setattr(item, "rep_" + rep.when, rep)


@pytest.fixture
def browser():
    with sync_playwright() as p:
        browser = p.chromium

        yield browser


@pytest.fixture(autouse=True)
def attach_screenshots_to_allure(request, t):
    yield

    if str(request.fspath).startswith(str(PROJECT_PATH.joinpath("tests/ui"))):
        if request.node.rep_call.failed:
            page = t.step.page._browser.contexts[0].pages[0]
            try:
                allure.attach(
                    body=page.screenshot(),
                    name=get_screenshot_name(request=request),
                    attachment_type=allure.attachment_type.PNG,
                )
            finally:
                page.close()


@pytest.fixture
def t(request, browser):
    if str(request.fspath).startswith(str(PROJECT_PATH.joinpath("tests/ui"))):
        browser_instance = browser.launch(headless=False, slow_mo=50)
        t_object = T(browser=browser_instance)
    else:
        browser_instance = None
        t_object = T()

    yield t_object

    if browser_instance is not None:
        browser_instance.close()
