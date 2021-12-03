import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import BasePage


class PythonPage(BasePage):
    url = "https://docs.python.org/3/"
    timeout = 10

    @property
    def _search_input(self):
        return self.driver.find_element_by_name("q")

    @property
    def _submit_button(self):
        return self.driver.find_element_by_xpath("/html/body/div[1]/ul/li[6]/div/form/input[2]")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    @allure.step
    def open(self):
        self.driver.get(self.url)

        # wait for accept policies popup and click accept
        WebDriverWait(driver=self.driver, timeout=self.timeout).until(
            expected_conditions.visibility_of_element_located(
                (By.XPATH, "/html/body/div[1]/ul/li[6]/div/form/input[2]")
            )
        )

    @allure.step
    def search_text(self, text: str):
        self._search_input.send_keys(text)
        self._submit_button.submit()
        WebDriverWait(driver=self.driver, timeout=self.timeout).until(
            expected_conditions.text_to_be_present_in_element(
                locator=(By.XPATH, '//*[@id="search-results"]/h2'), text_="Search Results"
            )
        )

    @allure.step
    def get_text_after_search(self):
        return self.driver.find_element_by_name("q").get_attribute("value")

    @allure.step
    def get_first_search_result(self):
        results_list = self.driver.find_element_by_class_name("search")
        link = results_list.find_element_by_tag_name("a")
        href = link.get_attribute("href")
        return href

    @allure.step
    def get_number_of_results(self):
        results_list = self.driver.find_element_by_class_name("search")
        links = results_list.find_elements_by_tag_name("a")
        return len(links)
