from behave import *
from selenium import webdriver


@given('launch the Chrome browser')
def step_impl(context):
    context.driver = webdriver.Chrome()


@when(u'I open the login page')
def step_impl(context):
    context.driver.get("https://vsmonitor.com/")


@when('I fill in the "{email}" and I fill in the "{password}"')
def step_impl(context, email, password):
    context.driver.find_element_by_id("email").send_keys(email)
    context.driver.find_element_by_id("password").send_keys(password)


@when('I click the login button')
def step_impl(context):
    context.driver.find_element_by_id("login-button").click()


@then('I must successfully login to the dashboard page')
def step_impl(context):
    text = context.driver.find_elements_by_link_text("https://vsmonitor.com/").text
    assert text == "Dashboard"
    context.driver.close()
