from selenium import webdriver
from behave import when, then, given
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from pages.login_page_orange import LoginPage_orange
from selenium.webdriver.common.by import By
import time


def setup_driver(context):
    try:
        chrome_options = ChromeOptions()
        chrome_options.add_argument("--start-maximized")
        chrome_options.add_argument("--disable-notifications")
        chrome_options.add_argument("--disable-extensions")

        chrome_service = ChromeService(executable_path = r'C:\\Users\\USER\\Desktop\\QA Automation\\Test-Automation-with-Selenium-for-QA-Python-\\Projects List\\Project_login_test_orangeHRM\\driver\\chromedriver.exe')


        context.driver = webdriver.Chrome(service=chrome_service,options=chrome_options)
        return context.driver
    except Exception as e:
        print(f"An error has occured in setup driver: {e}")

@given(u'I Open login page')
def step_imp(context):
    try:
        context.driver = setup_driver(context)
        context.driver.get("https://subasinghe123-osondemand.orangehrm.com/")
        time.sleep(8)
        context.login_page_orange = LoginPage_orange(context.driver)

    except Exception as e:
        print(f"an error has occured in open login page: {e}")

@when(u'I Type username \'Admin\' into Username field')
def step_imp(context):
    context.login_page_orange.enter_username("Admin")
    
@when(u'I Type username \'incorrectUser\' into Username field')
def step_imp(context):
    context.login_page_orange.enter_username("incorrectUser")

@when(u'I Type password \'@6f@D7@jnSPN\' into Password field')
def step_imp(context):
    context.login_page_orange.enter_password("@6f@D7@jnSPN")

@when(u'I Type password \'incorrectPassword\' into Password field')
def step_imp(context):
    context.login_page_orange.enter_password("incorrectPassword")    

@when(u'I Push Login button')
def step_imp(context):
    context.login_page_orange.click_login_button()

@when(u'I Verify new page URL contains orangehrm.com/dashboard/index')
def step_imp(context):
    Expected_url = "https://subasinghe123-osondemand.orangehrm.com/dashboard/index"
    Actual_url = context.driver.current_url
    assert Actual_url == Expected_url, "Actual page URL is not the same as expected"

@when(u'I Verify new page contains expected text (\'Dashboard\' or \'successfully logged in\')')
def step_imp(context):
    # dashboard_element = context.driver.findelement(By.ID,"//*[@id=\"app\"]/div[1]/div[1]/header/div[1]/div[1]/span/h6")
    dashboard_element = context.driver.find_element(By.XPATH,"//*[@id=\"app\"]/div[2]/div[1]/header/div[1]/div[1]/span/h6")

    assert dashboard_element.is_displayed(), "Dashboard is not displayed"

@then(u'I Verify button Log out is displayed on the new page')
def step_imp(context):
    context.driver.find_element(By.XPATH,"//*[@id=\"app\"]/div[2]/div[1]/header/div[1]/div[3]/ul/li").click()
    time.sleep(3)
    logout_element = context.driver.find_element(By.XPATH,"//*[@id=\"app\"]/div[2]/div[1]/header/div[1]/div[3]/ul/li/ul/li[4]/a")    

    assert logout_element.is_displayed(), "Log out button is not displayed"

@then(u'I Verify error message for username is displayed')
def step_imp(context):
    error_message = "Invalid credentials"
    username_error = context.login_page_orange.get_error_msg()
    # username_error = context.driver.find_element(By.LINK_TEXT,"Invalid credentials")

    assert username_error == error_message, "username error is not diplayed"

@then(u'I Verify error message for password is displayed')
def step_imp(context):
    error_message = "Invalid credentials"
    password_error = context.login_page_orange.get_error_msg()
    # password_error = context.driver.find_element(By.LINK_TEXT,"Invalid credentials")

    assert password_error == error_message, "password error is not diplayed"

# @then(u'I Verify error message text is "Your username is invalid!"')
# def step_imp(context):


# @then(u'I Verify error message text is "Your password is invalid!"')
# def step_imp(context):
        

# I Verify error message text is 'Your username is invalid!'
# I Verify error message text is 'Your password is invalid!'





