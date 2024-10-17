from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.select import Select

from browser import Browser


class BasePage(Browser):

    # Pasam instanta unica de driver catre orice page object
    def __init__(self, webdriver):
        self.driver = webdriver

    def find(self, locator):
        return self.driver.find_element(*locator)

    def find_all(self, locator) -> list[WebElement]:
        return self.driver.find_elements(*locator)

    def type(self, locator, text):
        self.find(locator).send_keys(text)

    def click(self, locator):
        self.find(locator).click()

    def verify_current_url(self, expected_url):
        return self.driver.current_url == expected_url

    def is_element_absent(self, locator):
        return len(self.find_all(locator)) == 0

    def select_dropdown_item_by_text(self, locator, text):
        dropdown = Select(self.find(locator))
        dropdown.select_by_visible_text(text)
