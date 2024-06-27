from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from behave import given, when , then

import time


def setup_driver(context):
    
    context.service = ChromeService(ChromeDriverManager().install())
    # driverpath = "C:\\Users\\USER\\Desktop\\QA Automation\\Test-Automation-with-Selenium-for-QA-Python-\\Projects List\\Project_assessment\\driver\\chromedriver.exe"
    # service = Service(driverpath)
    options = Options()
    # options.add_argument('--headless=new')
    # context.driver = webdriver.Chrome(service=service,options=options)
    context.driver = webdriver.Chrome(service=context.service,options=options)
    return context.driver

@given('User goes to google.lk site')
def open_browser(context):
    
    context.driver = setup_driver(context)
    context.driver.maximize_window()
    context.driver.get('https://www.google.lk/')

@when('User types "eLearning.lk" in Google and clicks the "eLearning.lk" link')
def explore_google(context):

    context.wait = WebDriverWait(context.driver,10)

    google_search = context.wait.until(EC.element_to_be_clickable((By.ID, 'APjFqb')))
    google_search.send_keys("elearning.lk")
    print("----Typed: elearning.lk on google search----")

    google_search_button = context.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'gNO89b')))
    google_search_button.click()
    print("----Google search button is clicked----")

    e_link = context.wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id=\"rso\"]/div[1]/div/div/div/div/div/div/div/div[1]/div/span/a/h3')))
    e_link.click()
    print("----Searched link of elearing.lk is clicked----")


@then('User searches for the Python course in the eLearning.lk search bar')
def explore_elearning(context):

    context.wait = WebDriverWait(context.driver,5) 

    view_all_courses = context.wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="navbarCollapse"]/ul/li[2]')))
    view_all_courses.click()
    print("----courses menu opened----")

    time.sleep(1)

    search_course = context.wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="course_search"]')))
    #Type 'Python' into the search bar and press Enter
    search_course.send_keys("Python Course")    
    search_course.send_keys(Keys.RETURN)
    print("----searching python course----")

    time.sleep(1)
    
    python_course = context.wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="course-menu"]/div/div/div[2]/div[1]/div/div/a')))
    python_course.click()
    print("----python course clicked----")

    actions = ActionChains(context.driver)
    actions.send_keys(Keys.PAGE_DOWN).perform()
    actions.send_keys(Keys.PAGE_DOWN).perform()

    print("----page scrolled down----")

    
@then('User clicks on the Python course and generate a report of the course content after checking')
def elearning_course(context):
    # Set up an explicit wait of 5 seconds
    context.wait = WebDriverWait(context.driver, 5) 

    # Initialize an empty list to store the course content elements
    course_content_elements = []

    # Loop through the child elements from the 20th to the 31st
    for i in range(20, 32):
        # Wait until the elements matching the CSS selector are present in the DOM
        elements = context.wait.until(EC.presence_of_all_elements_located(
            (By.CSS_SELECTOR, f'#course-title-section > div > div > div > div.we-single-content > p:nth-child({i})')
        ))
        # Extend the list with the newly found elements
        course_content_elements.extend(elements)

    # Extract the text from each course content element
    course_content = [element.text for element in course_content_elements]

    # Open a text file in write mode
    with open('python_course_report.txt', 'w') as file:
        # Write each content to the file followed by a newline
        for content in course_content:
            file.write(f"{content}\n")

    print("report generated")
    
    time.sleep(4)
    # Close the browser
    context.driver.quit()



