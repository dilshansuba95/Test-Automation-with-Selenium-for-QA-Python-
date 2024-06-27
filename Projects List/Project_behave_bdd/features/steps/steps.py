from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait #WebDriverWait: Used to wait for certain conditions (like element visibility) before proceeding.
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import sys
from behave import given , when , then
#context: A Behave-specific object that stores information and state throughout the execution of steps.
#assert statements: Check if conditions are met; if not, an AssertionError is raised, indicating a test failure.

#Initializes the Chrome WebDriver using ChromeDriverManager,
#Which automatically manages the driver binary.
def setup_driver(context):
    # Creates a ChromeService object using the ChromeDriverManager.
    # The ChromeDriverManager().install() method will download the latest
    # version of the ChromeDriver executable if it's not already present..
    context.service = ChromeService(ChromeDriverManager().install())
    # Returns a Chrome WebDriver instance specifying the service to use.
    # This WebDriver is what you'll use to interact with the Chrome browser.
    return webdriver.Chrome(service=context.service)

#Given steps: Define the initial state before an event (when step) occurs.
#In this case, navigating to ‘python.org’.
@given('we go to python.org site')
def open_browser(context):
    # context.service = webdriver.ChromeService(executable_path = 'C:\\Users\\USER\\Desktop\\QA Automation\\Project3withdriverzip\\Project3\\driver\\chromedriver.exe')
    # context.driver = webdriver.Chrome(service=context.service)
    context.driver = setup_driver(context)
    context.driver.maximize_window()
    context.driver.get('https://www.python.org/')
#When steps: Define the event that triggers the state change.
#Here, clicking on the ‘downloads’ link on ‘python.org’.
@when('we click downloads')
def click_downloads(context):
    context.wait = WebDriverWait(context.driver, 30)
    downloads_link = context.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id=\"downloads\"]")))
    downloads_link.click()
    print('~~~~~~ Downloads link Clicked')
    print(str(context.driver.current_url))
    assert str(context.driver.current_url) == 'https://www.python.org/downloads/'

#Then steps: Define the expected outcome after the when step. For example,
#verifying that ‘Download Python 3.12.4’ is available.
@then('we should download python 3.12.4')
#def click_download_python(driver , python_version):
def click_download_python(context):
    context.wait = WebDriverWait(context.driver, 30)
    download_python_button = context.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id=\"touchnav-wrapper\"]/header/div/div[2]/div/div[2]/p/a")))
    print('~~~~~~~~~~~~~~~~')
    print(download_python_button.text)
    if 'Download Python 3.12.4' == download_python_button.text :
        print('Test Case Passed')
        assert True
    else:
        print('Test Case Failed. The version avaialable to download is'+ download_python_button.text)
        assert False
    context.driver.close()