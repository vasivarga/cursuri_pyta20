from behave import *

@given('I am on the login page')
def step_impl(context):
    context.login_page.open()

@when('I enter "{text}" as username')
def step_impl(context, text):
    context.login_page.set_username(text)

@when('I enter "{text}" as password')
def step_impl(context, text):
    context.login_page.set_password(text)

@when('I click on login button')
def step_impl(context):
    context.login_page.click_login_button()

@then('The url of the current page is "{url}"')
def step_impl(context, url):
    assert context.login_page.verify_current_url(url)

@then('I see login error with text "{message}"')
def step_impl(context, message):
    assert context.login_page.get_login_error_text() == message

