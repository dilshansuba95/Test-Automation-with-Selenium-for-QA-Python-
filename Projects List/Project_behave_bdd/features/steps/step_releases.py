from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from behave import given , when , then


@when('we click source code from Downloads menu')
def click_source_code(context):
    context.wait = WebDriverWait(context.driver, 30)
    downloads_link = context.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id=\"downloads\"]")))
    actions = ActionChains(context.driver)
    actions.move_to_element(downloads_link).perform()
    source_code_link = context.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id=\"downloads\"]/ul/li[2]/a")))
    source_code_link.click()
    print('~~~~~~ Source Code link Clicked')
    print(str(context.driver.current_url))
    assert str(context.driver.current_url) == 'https://www.python.org/downloads/source/'

@then('we search for the "{latest_relase}" in source')
def search(context,latest_relase):
    context.wait = WebDriverWait(context.driver, 30)
    search_feild = context.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id=\"id-search-field\"]")))
    search_feild.send_keys(latest_relase)
    print('~~~~~~ Searching for Text')
    GO_button = context.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id=\"submit\"]")))
    GO_button.click()
    for i in range(1, 21):
        print(i)
        try:
            serch_xpath = "//*[@id=\"content\"]/div/section/form/ul/li["+str(i)+"]/h3/a"
            search_result = context.wait.until(EC.element_to_be_clickable((By.XPATH,serch_xpath)))
            print(search_result.text)
            if latest_relase == search_result.text :
                print('Match')
                assert True
                break
            else:
                print('No Math')
        except:
            print()
            assert False
