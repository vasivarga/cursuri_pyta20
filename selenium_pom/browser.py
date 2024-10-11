from selenium import webdriver


class Browser:

    # Aici setam driver-ul ca variabila de clasa
    # iar valoarea ei va fi None la inceput
    def __init__(self):
        self.driver = None

    # Pornire browser - se va apela doar in BasePage
    def get_driver(self):
        # Deschidem driver nou numai daca nu avem deja unul deschis
        # In clasa ProductTests am declarat doua page objects: login_page si products_page
        # Daca nu punem acest if, se vor deschide 2 browsere cand rulam toata clasa de teste.
        if self.driver is None:
            self.driver = webdriver.Chrome()  
            self.driver.maximize_window()
            self.driver.implicitly_wait(3)
        return self.driver

    def close_browser(self):
        if self.driver:
            self.driver.quit()
            self.driver = None
