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

# driverpath = "C:\\Users\\USER\\Desktop\\QA Automation\\Test-Automation-with-Selenium-for-QA-Python-\\Projects List\\Project_assessment\\driver\\chromedriver.exe"
# service = Service(driverpath)
# options.add_argument('--headless=new')
# context.driver = webdriver.Chrome(service=service,options=options)

def setup_driver(context):
    try:
        # Set up ChromeDriver service
        chrome_service = ChromeService(ChromeDriverManager().install())

        # Set up Chrome options
        chrome_options = Options()
        chrome_options.add_argument("--start-maximized")  # Start browser maximized
        chrome_options.add_argument("--disable-infobars")  # Disable infobars
        chrome_options.add_argument("--disable-extensions")  # Disable extensions

        # Initialize WebDriver
        context.driver = webdriver.Chrome(service=chrome_service, options=chrome_options)
        return context.driver
    except Exception as e:
        print(f"An error occurred while setting up the driver: {e}")


@given('User goes to google.lk site')
def open_browser(context):
    try:
        context.driver = setup_driver(context)  # Set up the WebDriver
        # Navigate to Google.lk
        context.driver.get('https://www.google.lk/')
    except Exception as e:
        print(f"An error occurred while opening the browser: {e}")


@when('User types "eLearning.lk" in Google and clicks the "eLearning.lk" link')
def explore_google(context):
    try:
        context.wait = WebDriverWait(context.driver, 10)

        # Locate the Google search bar and enter the search term
        search_bar = context.wait.until(EC.element_to_be_clickable((By.ID, 'APjFqb')))
        search_bar.send_keys("elearning.lk")
        print("----Typed: elearning.lk on Google search----")

        # Click the Google search button
        search_button = context.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'gNO89b')))
        search_button.click()
        print("----Google search button is clicked----")

        # Click the first search result link
        first_result_link = context.wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="rso"]/div[1]/div/div/div/div/div/div/div/div[1]/div/span/a/h3')))
        first_result_link.click()
        print("----Searched link of elearning.lk is clicked----")
    except Exception as e:
        print(f"An error occurred in explore_google: {e}")


@then('User searches for the Python course in the eLearning.lk search bar')
def explore_elearning(context):
    try:
        context.wait = WebDriverWait(context.driver, 5)

        # Open the courses menu
        courses_menu = context.wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="navbarCollapse"]/ul/li[2]')))
        courses_menu.click()
        print("----courses menu opened----")

        time.sleep(1)

        # Locate the search bar and enter the search term
        search_bar = context.wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="course_search"]')))
        search_bar.send_keys("Python Course")
        search_bar.send_keys(Keys.RETURN)
        print("----searching python course----")

        time.sleep(1)

        # Click the Python course link
        python_course_link = context.wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="course-menu"]/div/div/div[2]/div[1]/div/div/a')))
        python_course_link.click()
        print("----python course clicked----")

        # Scroll down the page
        actions = ActionChains(context.driver)
        actions.send_keys(Keys.PAGE_DOWN).perform()
        actions.send_keys(Keys.PAGE_DOWN).perform()
        print("----page scrolled down----")
    except Exception as e:
        print(f"An error occurred in explore_elearning: {e}")

    
@then('User clicks on the Python course and generate a report of the course content after checking')
def elearning_course(context):
    try:
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
    except Exception as e:
        print(f"An error occurred in elearning_course: {e}")



