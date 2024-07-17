from behave import given, when, then
from selenium import webdriver
from pages.login_page import LoginPage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


def setup_driver(context):
    try:
        # Set up ChromeDriver service
        chrome_service = ChromeService(ChromeDriverManager().install())

        # Set up Chrome options
        chrome_options = Options()
        chrome_options.add_argument("--start-maximized")  # Start browser maximized
        chrome_options.add_argument("--disable-notifications")  # Disable notifications
        chrome_options.add_argument("--disable-extensions")  # Disable extensions

        # Initialize WebDriver
        context.driver = webdriver.Chrome(service=chrome_service, options=chrome_options)
        return context.driver
    except Exception as e:
        print(f"An error occurred while setting up the driver: {e}")

@given('I am on the login page')
def step_impl(context):
    try:
        context.driver = setup_driver(context)  # Set up the WebDriver
        # Navigate to blazedeom login
        context.driver.get("https://blazedemo.com/login")
        context.login_page = LoginPage(context.driver)
    except Exception as e:
        print(f"An error occurred while opening the browser: {e}")


@when('I enter a valid email and password')
def step_impl(context):
    context.login_page.enter_email("valid@example.com")
    context.login_page.enter_password("validpassword")

@when('I enter an invalid email and password')
def step_impl(context):
    context.login_page.enter_email("invalid@example.com")
    context.login_page.enter_password("invalidpassword")

@when('I enter edge case email and password')
def step_impl(context):
    context.login_page.enter_email("edgecase@example.com")
    context.login_page.enter_password("edgecasepassword")

@when('I click remember me')
def step_impl(context):
    context.login_page.click_remember_me()

@when('I click the login button')
def step_impl(context):
    context.login_page.click_login()

@then('I should be logged in successfully')
def step_impl(context):
    # Add assertion for successful login
    pass
    # Example: Check if the URL has changed to the dashboard page
    #assert context.driver.current_url == "http://example.com/dashboard"

    # Example: Check if a specific element is present on the dashboard page
    #dashboard_element = context.driver.find_element_by_id("dashboard")
    #assert dashboard_element.is_displayed()

@then('I should see an error message')
def step_impl(context):
    error_message = context.login_page.get_error_message()
    assert error_message == "Page Expired"

@then('I should see an appropriate error message')
def step_impl(context):
    error_message = context.login_page.get_error_message()
    assert error_message == "Invalid credentials"