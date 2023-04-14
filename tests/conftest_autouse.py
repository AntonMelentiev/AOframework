import allure
import pytest

from framework.utils.allure_helpers import get_screenshot_name


@pytest.fixture(autouse=True)
def attach_screenshots_to_allure(request, browser):
    yield

    if request.node.rep_call.failed:
        page = browser.contexts[0].pages[0]  # TODO: check if it's correct
        try:
            allure.attach(
                body=page.screenshot(),
                name=get_screenshot_name(request=request),
                attachment_type=allure.attachment_type.PNG,
            )
        finally:
            page.close()
