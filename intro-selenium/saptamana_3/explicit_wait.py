import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class ExplicitWaitDemo(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.get("https://the-internet.herokuapp.com/dynamic_loading")

    def tearDown(self) -> None:
        self.driver.quit()

    def test_hidden_element(self):
        self.driver.find_element(By.PARTIAL_LINK_TEXT, "Example 1").click()
        self.driver.find_element(By.XPATH, "//button[text()='Start']").click()

        # Exemplu gresit - implicit wait nu ne ajuta in acest caz
        # self.driver.implicitly_wait(10)
        # assert self.driver.find_element(By.ID, "finish").is_displayed()
        locator = (By.ID, "finish")
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located(locator))
        # wait.until(EC.visibility_of(self.driver.find_element(*locator)))

        self.assertTrue(self.driver.find_element(*locator).is_displayed())

    def test_missing_element(self):
        self.driver.find_element(By.PARTIAL_LINK_TEXT, "Example 2").click()
        self.driver.find_element(By.XPATH, "//button[text()='Start']").click()
        locator = (By.ID, "finish")

        # self.driver.implicitly_wait(10)
        # assert self.driver.find_element(By.ID, "finish").is_displayed()
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located(locator))
        self.assertTrue(self.driver.find_element(*locator).is_displayed())


