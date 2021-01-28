from behave import *
from selenium import webdriver


@given('Launch the Chrome browser')
def step_impl(context):
    context.driver = webdriver.Chrome(executable_path="C:\\DRIVERS\\chromedriver.exe")


@when('Open a orange HRM homepage')
def step_impl(context):
    context.driver.get("https://opensource-demo.orangehrmlive.com/")
    context.driver.maximize_window()


@when('Enter username "{user}" and password "{pwd}"')
def step_impl(context, user, pwd):
    context.driver.find_element_by_xpath("//input[@id='txtUsername']").send_keys(user)
    context.driver.find_element_by_xpath("//input[@id='txtPassword']").send_keys(pwd)


@when('click on login button')
def step_impl(context):
    context.driver.find_element_by_xpath('//input[@id="btnLogin"]').click()


@then('User must successfully login to the dashboard page')
def step_impl(context):
    try:
        text = context.driver.find_element_by_xpath('//h1[text()="Dashboard"]').text
    except:
        context.driver.close()
        assert False,"Test Failed"

    if text == "Dashboard":
        context.driver.close()
        assert True,"Test Passed"
