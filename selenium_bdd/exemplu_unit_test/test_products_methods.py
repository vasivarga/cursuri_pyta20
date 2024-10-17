import unittest

from browser import Browser
from pages.login_page import LoginPage
from pages.products_page import ProductsPage


class TestProductsPage(unittest.TestCase):

    def test_inverse_sort(self):
        driver = Browser().get_driver()
        login_page = LoginPage(driver)
        products_page = ProductsPage(driver)
        login_page.open()
        login_page.login("standard_user", "secret_sauce")
        products_page.sort_items("Name (Z to A)")
        products_page.verify_products_names_sorted_reverse_alphabetical()