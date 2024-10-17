from behave import *

@given('I am on the products page')
def step_impl(context):
    context.login_page.open()
    context.login_page.login("standard_user", "secret_sauce")

@then('Product names are sorted alphabetically')
def step_impl(context):
    context.products_page.verify_product_names_sorted_alphabetically()

@when('I sort the products "{text}"')
def step_impl(context, text):
    context.products_page.sort_items(text)

@then('Product names are sorted in inverse alphabetical order')
def step_impl(context):
    context.products_page.verify_products_names_sorted_reverse_alphabetical()

@then('Products are sorted by price (low to high)')
def step_impl(context):
    context.products_page.verify_product_price_sorted_low_to_high()