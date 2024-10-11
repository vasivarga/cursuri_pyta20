import unittest

from browser import Browser
from pages.login_page import LoginPage
from pages.products_page import ProductsPage


class ProductsTests(unittest.TestCase):

    def setUp(self) -> None:
        # Deoarece avem si login_page si products_page, trebuie sa evitam deschiderea a doua browsere
        # De aceea, declaram o singura instanta de driver, pe care o pasam in constructor la fiecare PageObject
        self.driver = Browser().get_driver()
        self.login_page = LoginPage(self.driver)
        self.products_page = ProductsPage(self.driver)

        self.login_page.open()
        self.login_page.login("standard_user", "secret_sauce")

    def tearDown(self) -> None:
        self.products_page.close_browser()

    def test_add_item_to_cart(self):
        self.products_page.click_add_to_cart_backpack_button()
        assert self.products_page.verify_shopping_cart_items_number(1)
        assert self.products_page.verify_add_to_cart_backpack_button_absent()
        assert self.products_page.verify_remove_backpack_button_visible()
        expected_title = self.products_page.get_backpack_title()

        self.products_page.click_shopping_cart()

        assert self.products_page.get_cart_item_name() == expected_title