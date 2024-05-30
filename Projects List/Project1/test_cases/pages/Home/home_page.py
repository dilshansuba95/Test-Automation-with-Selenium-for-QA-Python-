from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def click_downloads(driver):
    wait = WebDriverWait(driver, 30)
    downloads_link = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id=\"downloads\"]")))
    downloads_link.click()
    print('~~~~~~ Downloads link Clicked')
    print(str(driver.current_url))
    return driver

def search(driver,search_text):
    wait = WebDriverWait(driver, 30)
    search_feild = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id=\"id-search-field\"]")))
    search_feild.send_keys(search_text)
    print('~~~~~~ Searching for Text')
    GO_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id=\"submit\"]")))
    GO_button.click()
    # third_result = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id=\"content\"]/div/section/form/ul/li[3]/h3/a")))  
    third_result = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id=\"content\"]/div/section/form/ul/li[1]/h3/a")))  
    if search_text == third_result.text :
        print('Test Case Passed')
    else:
        print('Test Case Failed. The Searched result is'+ third_result.text)
    
    wait = WebDriverWait(driver, 30)


    # Python_news_link = wait.until(
    # EC.element_to_be_clickable((By.XPATH, "//*[@id=\"content\"]/div/section/form/ul/li[1]/h3/a"))
    # )
    Python_news_link = third_result
    Python_news_link.click()
    print(str(driver.current_url))
    return driver

def search_by_looping(driver,search_text):
    wait = WebDriverWait(driver, 30)
    search_feild = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id=\"id-search-field\"]")))
    search_feild.send_keys(search_text)
    print('~~~~~~ Searching for Text')
    GO_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id=\"submit\"]")))
    GO_button.click()
    for i in range(1, 21):
        print(i)
        try:
            search_xpath = "//*[@id=\"content\"]/div/section/form/ul/li["+str(i)+"]/h3/a"
            search_result = wait.until(EC.element_to_be_clickable((By.XPATH,search_xpath)))
            print(search_result.text)
            if search_text == search_result.text :
                print('Match')
                break
            else:
                print('No Match')
        except:
            print()

    return driver



    