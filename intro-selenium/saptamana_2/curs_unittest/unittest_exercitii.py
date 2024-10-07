import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By


class LoginTests(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Firefox()
        self.driver.get("https://the-internet.herokuapp.com/")
        self.driver.maximize_window()
        self.driver.find_element(By.LINK_TEXT, "Form Authentication").click()

    def tearDown(self) -> None:
        self.driver.quit()

    def test_url_is_correct(self):
        expected_result = "https://the-internet.herokuapp.com/login"
        actual_result = self.driver.current_url

        # assert expected_result == actual_result, "Unexpected URL"
        self.assertEqual(expected_result, actual_result, "Unexpected URL")

    def test_page_title(self):
        expected_title = "The Internet"
        actual_title = self.driver.title

        # assert expected_title == actual_title, "Unexpected title"
        self.assertEqual(expected_title, actual_title, "Unexpected title")

    def test_login_form_title(self):
        expected_text = "Login Page"
        element = self.driver.find_element(By.XPATH, "//h2")
        actual_text = element.text

        self.assertEqual(expected_text, actual_text, "Unexpected text")

    def test_invalid_login(self):
        self.driver.find_element(By.CLASS_NAME, "radius").click()

        error_element = self.driver.find_element(By.ID, "flash")

        # assert error_element.is_displayed(), "Element not visible"
        self.assertTrue(error_element.is_displayed(), "Element not visible")

        expected_text = "Your username is invalid!"
        actual_text = error_element.text

        # assert expected_text in actual_text, "Text not present"
        self.assertIn(expected_text, actual_text, "Text not present")

    # Lasam user si pass goale
    # Facem click pe butonul de login
    # Verificam ca apare eroarea
    # Facem click pe butonasul cu x ca sa dispara eroarea
    # Verificam ca eroarea a disparut
    def test_close_login_error(self):
        self.driver.find_element(By.CLASS_NAME, "radius").click()

        error_element = self.driver.find_element(By.ID, "flash")
        self.assertTrue(error_element.is_displayed(), "Element not visible")

        self.driver.find_element(By.CLASS_NAME, "close").click()

        time.sleep(1)

        assert self.is_absent((By.ID, "flash"))

    def test_successful_login(self):
        self.driver.find_element(By.ID, "username").send_keys("tomsmith")
        self.driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
        self.driver.find_element(By.CLASS_NAME, "radius").click()

        success_message = self.driver.find_element(By.CLASS_NAME, "success")

        # assert success_message.is_displayed()
        # assert "You logged into a secure area!" in success_message.text

        self.assertTrue(success_message.is_displayed())
        self.assertIn("You logged into a secure area!", success_message.text)


    def is_absent(self, locator) -> bool:
        lista_elemente = self.driver.find_elements(*locator)

        # return len(lista_elemente) == 0

        if len(lista_elemente) > 0:
            return False
        else:
            return True



