import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


class TestAlerts(unittest.TestCase):

    BUTTON_JS_ALERT = (By.CSS_SELECTOR, "[onclick='jsAlert()']")
    BUTTON_JS_CONFIRM = (By.CSS_SELECTOR, "[onclick='jsConfirm()']")
    BUTTON_JS_PROMPT = (By.CSS_SELECTOR, "[onclick='jsPrompt()']")
    P_RESULT = (By.ID, "result")

    def setUp(self) -> None:
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.get("https://the-internet.herokuapp.com/javascript_alerts")

    def tearDown(self) -> None:
        self.driver.quit()

    def find(self, locator) -> WebElement:
        return self.driver.find_element(*locator)

    def click(self, locator):
        self.find(locator).click()

    def test_accept_simple_alert(self):
        self.click(self.BUTTON_JS_ALERT)

        alert = self.driver.switch_to.alert
        alert.accept()

        self.assertEqual(self.find(self.P_RESULT).text, "You successfully clicked an alert")

    def test_dismiss_alert(self):
        self.click(self.BUTTON_JS_CONFIRM)

        alert = self.driver.switch_to.alert
        alert.dismiss()

        self.assertEqual(self.find(self.P_RESULT).text, "You clicked: Cancel")

    def test_prompt_alert(self):
        self.click(self.BUTTON_JS_PROMPT)

        alert = self.driver.switch_to.alert

        text_introdus = "Introducem un text"
        alert.send_keys(text_introdus)
        alert.accept()

        time.sleep(2)
        self.assertIn(text_introdus, self.find(self.P_RESULT).text)
