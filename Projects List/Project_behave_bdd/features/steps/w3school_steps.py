from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from behave import given , when , then


# @given('we go to w3school site')
# def open_browser(context):
#     driver_path = r'C:\Code\e-learning\Project3\driver\chromedriver.exe'
#     service = Service(driver_path)  # Correct instantiation of Service
#     options = Options()
#     options.add_argument('--headless=new')
#     context.driver = webdriver.Chrome(service=service, options=options)
#     context.driver.maximize_window()
#     context.driver.get('https://www.w3schools.com/')

def setup_driver(context):
    # Creates a ChromeService object using the ChromeDriverManager.
    # The ChromeDriverManager().install() method will download the latest
    # version of the ChromeDriver executable if it's not already present..
    context.service = ChromeService(ChromeDriverManager().install())
    options = Options()
    options.add_argument('--headless=new')
    
    # Returns a Chrome WebDriver instance specifying the service to use.
    # This WebDriver is what you'll use to interact with the Chrome browser.
    return webdriver.Chrome(service=context.service,options=options)

@given('we go to w3school site')
def open_browser(context):
    # context.service = webdriver.ChromeService(executable_path = 'C:\\Users\\USER\\Desktop\\QA Automation\\Project3withdriverzip\\Project3\\driver\\chromedriver.exe')
    # context.driver = webdriver.Chrome(service=context.service)
    context.driver = setup_driver(context)
    context.driver.maximize_window()
    context.driver.get('https://www.w3schools.com/')

@when('we search for "{search_text}" in global search')
def global_search(context,search_text):
    context.wait = WebDriverWait(context.driver, 30)
    global_search_text_box= context.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id=\"search2\"]")))
    global_search_text_box.send_keys(search_text)
    actions = ActionChains(context.driver)
    actions.move_to_element(global_search_text_box).perform()
    python_tutorial_link= context.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id=\"listofsearchresults\"]/a[1]")))
    python_tutorial_link.click()

@then('we check for "{tutorial_text}" in the page')
def check_for_text_in_python_page(context,tutorial_text):
    context.wait = WebDriverWait(context.driver, 30)
    print(str(context.driver.current_url))
    if context.driver.current_url == 'https://www.w3schools.com/python/default.asp':
        tutorail_text= context.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id=\"main\"]/div[3]/h2")))
        if tutorail_text.text == tutorial_text:
            assert True
        else:
            assert False
    else:
        assert False

