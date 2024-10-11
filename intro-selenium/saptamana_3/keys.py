import time
import unittest

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


class TestKeys(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.get("https://the-internet.herokuapp.com/key_presses")

    def tearDown(self) -> None:
        self.driver.quit()

    def test_keys(self):
        text_input = self.driver.find_element(By.ID, "target")

        text_input.send_keys("TestAutomation")

        # text_input.clear()
        text_input.send_keys(Keys.CONTROL + "A")
        time.sleep(1)
        text_input.send_keys(Keys.DELETE)
        time.sleep(1)

