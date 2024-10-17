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
    ITEM_PRICE = (By.CSS_SELECTOR, ".inventory_item_price")

    DROPDOWN_SORT = (By.CSS_SELECTOR, ".product_sort_container")

    def open(self):
        self.driver.get(PRODUCTS_PAGE_URL)

    def click_add_to_cart_backpack_button(self):
        self.click(self.ADD_TO_CART_BACKPACK_BUTTON)

    def verify_shopping_cart_items_number(self, number):
        assert self.find(self.SHOPPING_CART_BADGE).text == str(number)

    def verify_remove_backpack_button_visible(self):
        assert self.find(self.REMOVE_BACKPACK_BUTTON).is_displayed()

    def verify_add_to_cart_backpack_button_absent(self):
        assert self.is_element_absent(self.ADD_TO_CART_BACKPACK_BUTTON)

    def verify_remove_backpack_button_absent(self):
        assert self.is_element_absent(self.REMOVE_BACKPACK_BUTTON)

    def get_backpack_title(self):
        return self.find(self.BACKPACK_TITLE).text

    def click_shopping_cart(self):
        self.click(self.SHOPPING_CART)

    def get_cart_item_name(self):
        return self.find(self.ITEM_NAME).text

    def verify_product_names_sorted_alphabetically(self):
        list_all_items_elements = self.find_all(self.ITEM_NAME)

        # lista initiala in care punem elementele
        # asa cum sunt in pagina
        list_all_item_names = []

        for element in list_all_items_elements:
            list_all_item_names.append(element.text)

        assert self.is_sorted(list_all_item_names)


    def is_sorted(self, list_initial: list, inverse_sort=False):
        # copiez lista initiala intr-o alta lista
        # ca sa am ordinea din pagina web salvata
        list_copy = list_initial[:]

        # Sortam lista (presupunand ca poayte nu e sortata bine in pagina)
        list_initial.sort()

        # Daca vreau sa sortez lista invers atunci pun inverse_sort pe True
        if inverse_sort == True:
            list_initial.reverse()

        # Verificam ca cele doua liste sunt egale - adica ambele sortate
        return list_copy == list_initial

    def sort_items(self, text):
        self.select_dropdown_item_by_text(self.DROPDOWN_SORT, text)

    def verify_products_names_sorted_reverse_alphabetical(self):
        list_all_items_elements = self.find_all(self.ITEM_NAME)

        # lista initiala in care punem elementele
        # asa cum sunt in pagina
        list_all_item_names = []

        for element in list_all_items_elements:
            list_all_item_names.append(element.text)

        assert self.is_sorted(list_all_item_names, True)

    def verify_product_price_sorted_low_to_high(self):
        list_all_price_element = self.find_all(self.ITEM_PRICE)

        list_price_numeric = []

        for element in list_all_price_element:
            price = element.text.replace("$","")
            list_price_numeric.append(float(price))

        assert self.is_sorted(list_price_numeric)





