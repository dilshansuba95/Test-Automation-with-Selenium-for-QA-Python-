from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

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


@given('I am on the registration page')
def step_impl(context):
    try:
        context.driver = setup_driver(context)  # Set up the WebDriver
        # Navigate to blazedeom registration
        context.driver.get('https://blazedemo.com/register')
    except Exception as e:
        print(f"An error occurred while opening the browser: {e}")


@when('I enter "{name}" in the Name field')
def step_impl(context, name):
    context.driver.find_element(By.NAME, "name").send_keys(name)

@when(u'I enter "" in the Name field')
def step_impl(context):
    context.driver.find_element(By.NAME, "name").send_keys("")

@when('I enter "{company}" in the Company field')
def step_impl(context, company):
    context.driver.find_element(By.NAME, "company").send_keys(company)

@when(u'I enter "" in the Company field')
def step_impl(context):
    context.driver.find_element(By.NAME, "company").send_keys("")

@when('I enter "{email}" in the E-Mail Address field')
def step_impl(context, email):
    context.driver.find_element(By.NAME, "email").send_keys(email)

@when('I enter "{password}" in the Password field')
def step_impl(context, password):
    context.driver.find_element(By.NAME, "password").send_keys(password)

@when('I enter "" in the Password field')
def step_impl(context):
    context.driver.find_element(By.NAME, "password").send_keys("")

@when('I enter "{confirm_password}" in the Confirm Password field')
def step_impl(context, confirm_password):
    context.driver.find_element(By.ID, "password-confirm").send_keys(confirm_password)

@when('I enter "" in the Confirm Password field')
def step_impl(context):
    context.driver.find_element(By.ID, "password-confirm").send_keys("")

@when('I submit the registration form')
def step_impl(context):
    context.wait = WebDriverWait(context.driver, 5)
    submit_button = context.wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div/div/div/div/div[2]/form/div[6]/div/button')))
    submit_button.click()
    time.sleep(6)

@then('I should see a success message')
def step_impl(context):
    assert "Registration successful" in context.driver.page_source
    context.driver.quit()

@then('I should see an error message')
def step_impl(context):
    assert "Error" in context.driver.page_source
    context.driver.quit()

@then('I should see an appropriate message')
def step_impl(context):
    assert "Error" in context.driver.page_source or "Registration successful" in context.driver.page_source
    context.driver.quit()