import allure
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from framework.steps import Step
from framework.utils import get_screenshot_name


@pytest.fixture
def driver(request):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--incognito")
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
    driver.maximize_window()

    yield driver

    try:
        if request.node.rep_call.failed:
            allure.attach(
                driver.get_screenshot_as_png(),
                name=get_screenshot_name(request),
                attachment_type=allure.attachment_type.PNG,
            )
    finally:
        driver.quit()


@pytest.fixture
def step(driver):
    step = Step(driver=driver)

    yield step
