from jproperties import Properties #imports the Properties class from the jproperties library, which allows you to read configuration settings, from a properties file.
from selenium import webdriver #imports the webdriver class from the selenium library, which allows you to control a web browser programmatically.
from selenium.webdriver.common.keys import Keys #imports the Keys class from selenium, which provides access to special keyboard keys like 'ENTER'.
import sys #imports the sys module, which provides access to system-specific parameters and functions.
sys.path.append("C:\\QA Automation\\Project1_original\\Project1\\") #Adds a custom directory to the search path for Python modules.
from pages.Home.home_page import click_downloads , search , search_by_looping
from pages.Downloads.downloads_page import click_download_python

properties = Properties() #Creates an instance of the Properties class to work with the configuration file.

with open('testcase.properties', 'rb') as f:  #Opens the file named "testcase.properties" in binary read mode ('rb').
    properties.load(f, 'utf-8')              #loads the content of the properties file into the properties object, 
                                            #specifying the encoding as UTF-8.

test_url = properties.get('test_url')[0]  #Retrieves the value for the key "test_url" from the properties file and assigns it to the test_url variable
print(test_url)                          #Prints the retrieved test URL to the console.


def open_browser():  #This function sets up a Chrome webdriver instance using the specified path to the chromedriver.exe file
    service = webdriver.ChromeService(executable_path = 'C:\\Users\\USER\\Desktop\\QA Automation\\Project1_original\\Project1\\driver\\chromedriver.exe')
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()   #maximizes the browser window
    driver.get(test_url)      #opens the URL stored in the test_url variable 
    return driver            #returns the opened browser instance


def check_latest_python_version():
    python_version_text = "Download Python 3.12.3"
    driver = open_browser()
    driver = click_downloads(driver)
    driver = click_download_python(driver,python_version_text)
    driver.close()


def search_for_python_realses():
    search_text = "Python 2.5 Release"
    driver = open_browser()
    driver = search_by_looping(driver,search_text)
    driver.close()

def search_for_python_news():
    search_text = "Python News"
    driver = open_browser()
    driver = search(driver,search_text)
    driver.close()  

search_for_python_news()

search_for_python_realses()

#check_latest_python_version()




