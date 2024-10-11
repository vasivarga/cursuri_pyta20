from selenium.webdriver.common.by import By

from pages.base_page import BasePage

PRODUCTS_PAGE_URL = "https://www.saucedemo.com/inventory.html"

class ProductsPage(BasePage):

    ADD_TO_CART_BACKPACK_BUTTON = (By.ID, "add-to-cart-sauce-labs-backpack")
    SHOPPING_CART_BADGE = (By.CSS_SELECTOR, "span.shopping_cart_badge")
    REMOVE_BACKPACK_BUTTON = (By.ID, "remove-sauce-labs-backpack")
    BACKPACK_TITLE = (By.XPATH, "//button[@id='remove-sauce-labs-backpack']/../../div/a/div")
    SHOPPING_CART = (By.ID, "shopping_cart_container")

    ITEM_NAME = (By.CSS_SELECTOR, ".inventory_item_name")

    def open(self):
        self.driver.get(PRODUCTS_PAGE_URL)

    def click_add_to_cart_backpack_button(self):
        self.click(self.ADD_TO_CART_BACKPACK_BUTTON)

    def verify_shopping_cart_items_number(self, number):
        return self.find(self.SHOPPING_CART_BADGE).text == str(number)

    def verify_remove_backpack_button_visible(self):
        return self.find(self.REMOVE_BACKPACK_BUTTON).is_displayed()

    def verify_add_to_cart_backpack_button_absent(self):
        return self.is_element_absent(self.ADD_TO_CART_BACKPACK_BUTTON)

    def verify_remove_backpack_button_absent(self):
        return self.is_element_absent(self.REMOVE_BACKPACK_BUTTON)

    def get_backpack_title(self):
        return self.find(self.BACKPACK_TITLE).text

    def click_shopping_cart(self):
        self.click(self.SHOPPING_CART)

    def get_cart_item_name(self):
        return self.find(self.ITEM_NAME).text



