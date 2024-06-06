from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
import time

def click_downloads(driver):
    wait = WebDriverWait(driver, 30)
    downloads_link = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id=\"downloads\"]")))
    downloads_link.click()
    print('~~~~~~ Downloads link Clicked')
    print(str(driver.current_url))
    return driver

def click_all_releases(driver):
    wait = WebDriverWait(driver, 30)
    downloads_link = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id=\"downloads\"]")))
    actions = ActionChains(driver)
    actions.move_to_element(downloads_link).perform()
    all_relases_link = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id=\"downloads\"]/ul/li[1]/a")))
    all_relases_link.click()
    print('~~~~~~ All releases link Clicked')
    print(str(driver.current_url))
    time.sleep(2)
    return driver

def click_source_code(driver):
    wait = WebDriverWait(driver, 30)
    downloads_link = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id=\"downloads\"]")))
    actions = ActionChains(driver)
    actions.move_to_element(downloads_link).perform()
    source_code_link = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id=\"downloads\"]/ul/li[2]/a")))
    source_code_link.click()
    print('~~~~~~ Source Code link Clicked')
    print(str(driver.current_url))
    time.sleep(2)
    return driver

def click_windows(driver):
    wait = WebDriverWait(driver, 30)
    downloads_link = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id=\"downloads\"]")))
    actions = ActionChains(driver)
    actions.move_to_element(downloads_link).perform()
    windows_link = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id=\"downloads\"]/ul/li[3]/a")))
    windows_link.click()
    print('~~~~~~ Windows link Clicked')
    print(str(driver.current_url))
    time.sleep(2)
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
    
    #wait = WebDriverWait(driver, 30)


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



    