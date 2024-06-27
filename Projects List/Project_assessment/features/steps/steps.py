from selenium import webdriver
# from selenium.webdriver.chrome.service import Service as ChromeService
# from webdriver_manager.chrome import ChromeDriverManager
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
    
    # context.service = ChromeService(ChromeDriverManager().install())
    driverpath = "C:\\Users\\USER\\Desktop\\QA Automation\\Test-Automation-with-Selenium-for-QA-Python-\\Projects List\\Project_assessment\\driver\\chromedriver.exe"
    service = Service(driverpath)
    options = Options()
    # options.add_argument('--headless=new')
    context.driver = webdriver.Chrome(service=service,options=options)
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
    
    context.wait = WebDriverWait(context.driver,5) 
    # Wait until the course content is present
    content_element_1 = context.wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '#course-title-section > div > div > div > div.we-single-content > p:nth-child(20)')))
    content_elements_2 = context.wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '#course-title-section > div > div > div > div.we-single-content > p:nth-child(21)')))
    content_elements_3 = context.wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '#course-title-section > div > div > div > div.we-single-content > p:nth-child(22)')))
    content_elements_4 = context.wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '#course-title-section > div > div > div > div.we-single-content > p:nth-child(23)')))
    content_elements_5 = context.wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '#course-title-section > div > div > div > div.we-single-content > p:nth-child(24)')))
    content_elements_6 = context.wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '#course-title-section > div > div > div > div.we-single-content > p:nth-child(25)')))
    content_elements_7 = context.wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '#course-title-section > div > div > div > div.we-single-content > p:nth-child(26)')))
    content_elements_8 = context.wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '#course-title-section > div > div > div > div.we-single-content > p:nth-child(27)')))
    content_elements_9 = context.wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '#course-title-section > div > div > div > div.we-single-content > p:nth-child(28)')))
    content_elements_10 = context.wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '#course-title-section > div > div > div > div.we-single-content > p:nth-child(29)')))
    content_elements_11 = context.wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '#course-title-section > div > div > div > div.we-single-content > p:nth-child(30)')))
    content_elements_12 = context.wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '#course-title-section > div > div > div > div.we-single-content > p:nth-child(31)')))


    course_content_elements = content_element_1 + content_elements_2 + content_elements_3 + content_elements_4 + content_elements_5 + content_elements_6 + content_elements_7 + content_elements_8 + content_elements_9 + content_elements_10 + content_elements_11 + content_elements_12

    # Extract text from each course content element
    course_content = [element.text for element in course_content_elements]

    # Write the course content to a text file
    with open('python_course_report.txt', 'w') as file:
        for content in course_content:
            file.write(f"{content}\n")
    print("report generated")
    # Close the browser
    time.sleep(5)
    context.driver.quit()



