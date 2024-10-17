from browser import Browser
from pages.login_page import LoginPage
from pages.products_page import ProductsPage


def before_scenario(context, scenario):
    context.driver = Browser().get_driver()
    context.login_page = LoginPage(context.driver)
    context.products_page = ProductsPage(context.driver)

def after_scenario(context, scenario):
    context.login_page.close_browser()