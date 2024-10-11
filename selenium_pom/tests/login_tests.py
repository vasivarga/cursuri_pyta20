import unittest

from browser import Browser
from pages.login_page import LoginPage, LOGIN_PAGE_URL

LOGIN_ERROR_MESSAGE = "Epic sadface: Username and password do not match any user in this service"
LOCKED_OUT_ERROR_MESSAGE = "Epic sadface: Sorry, this user has been locked out."

class LoginTests(unittest.TestCase):

    def setUp(self) -> None:
        # declaram o singura instanta de driver, pe care o pasam in constructor la fiecare PageObject
        self.driver = Browser().get_driver()
        self.login_page = LoginPage(self.driver)
        self.login_page.open()

    def tearDown(self) -> None:
        self.login_page.close_browser()

    def test_successful_login(self):
        # self.login_page.set_username("standard_user")
        # self.login_page.set_password("secret_sauce")
        # self.login_page.click_login_button()
        self.login_page.login("standard_user", "secret_sauce")
        assert self.login_page.verify_current_url("https://www.saucedemo.com/inventory.html")

    def test_login_with_invalid_password(self):
        self.login_page.login("standard_user", "sjdhfuwehrfuweh")
        assert self.login_page.verify_current_url(LOGIN_PAGE_URL)
        assert self.login_page.get_login_error_text() == LOGIN_ERROR_MESSAGE

    def test_login_with_locked_out_user(self):
        self.login_page.login("locked_out_user", "secret_sauce")
        assert self.login_page.verify_current_url(LOGIN_PAGE_URL)
        assert self.login_page.get_login_error_text() == LOCKED_OUT_ERROR_MESSAGE

    def test_login_with_invalid_username(self):
        self.login_page.login("user_random_inexistent", "secret_sauce")
        assert self.login_page.verify_current_url(LOGIN_PAGE_URL)
        assert self.login_page.get_login_error_text() == LOGIN_ERROR_MESSAGE
