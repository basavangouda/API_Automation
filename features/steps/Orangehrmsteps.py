from behave import *
from selenium import webdriver

# Admin
# admin123

@given('launch Chrome Browser')
def LaunchBrowser(context):
    context.driver = webdriver.Chrome(executable_path="C:\\DRIVERS\\chromedriver.exe")

@when('open Orange HRM HomePage')
def OpenHomePage(context):
    context.driver.get("https://opensource-demo.orangehrmlive.com/")

@then('verify the logo present on the home page')
def VerifyLogo(context):
    st=context.driver.find_element_by_xpath("//div[@id='divLogo']/img").is_displayed()
    assert st is True

@then('close browser')
def closeBrowser(context):
    context.driver.close()

