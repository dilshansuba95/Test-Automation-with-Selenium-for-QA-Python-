from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def setup_driver():
    service = ChromeService(ChromeDriverManager().install())
    return webdriver.Chrome(service=service)

def open_url(driver, url):
    driver.get(url)

def search_google(driver, query):
    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys(query)
    search_box.submit()

def open_new_tab(driver, url):
    driver.execute_script(f"window.open('{url}', '_blank');")
    driver.switch_to.window(driver.window_handles[1])

def previous_tab(driver):
    driver.switch_to.window(driver.window_handles[0])

def select_option_by_visible_text(driver, xpath, option_text):
    dropdown_element = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.XPATH, xpath))
    )
    select = Select(dropdown_element)
    select.select_by_visible_text(option_text)

def click_find_flights_button(driver, xpath):
    button = WebDriverWait(driver,3).until(
        EC.element_to_be_clickable((By.XPATH, xpath))
    )
    button.click()

def click_first_result(driver):
    first_result = driver.find_element(By.XPATH, "(//h3)[1]")
    inner_text = first_result.get_attribute("innerText")
    print("Inner text of the element is:", inner_text)
    if first_result.is_enabled():
        print("The element is enabled")
        first_result.click()
    else:
        print("The element is not enabled")
        
def expected_title(driver, url):
    act_title = driver.title
    exp_title = f"{url}"
    try:
        if exp_title == act_title:
            print("Test passed")
        else:
            print("Test Failed")
    except Exception as Exc:
        print(f"Exception occured: {Exc}")


if __name__ == "__main__":
    try:
        driver = setup_driver()
        open_url(driver, "http://www.google.com")
        search_google(driver, "Selenium Python")
        print("---(1)---")
        print(driver.current_url)
        time.sleep(3)

        open_new_tab(driver, "https://blazedemo.com/")
        select_option_by_visible_text(driver, "/html/body/div[3]/form/select[1]", "Mexico City")
        select_option_by_visible_text(driver, "/html/body/div[3]/form/select[2]", "London")
        click_find_flights_button(driver, "/html/body/div[3]/form/div/input")
        expected_title(driver,"BlazeDemo - reserve")
        time.sleep(3)
        print("---(2)---")
        print(driver.current_url)
        previous_tab(driver)
        click_first_result(driver)
        time.sleep(2)

    finally:
        driver.quit()


# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service as ChromeService
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import Select
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import time

# # Set up ChromeDriver using ChromeDriverManager
# service = ChromeService(ChromeDriverManager().install())
# driver = webdriver.Chrome(service=service)

# try:
#     # Open the first URL in the original tab
#     driver.get("http://www.google.com")

#     # Perform an action on the original tab (e.g., searching for something)
#     search_box = driver.find_element(By.NAME, "q")
#     search_box.send_keys("Selenium Python")
#     search_box.submit()

#     print("---(1)---")
#     print(driver.current_url)

#     # Wait for a few seconds to see the results
#     time.sleep(3)

#     # Open a new tab and switch to it
#     driver.execute_script("window.open('https://blazedemo.com/', '_blank');")
#     driver.switch_to.window(driver.window_handles[1])

#     wait = WebDriverWait(driver, 5)

#     # Locate the dropdown element by its ID
#     dropdown_element = wait.until(
#          EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/form/select[1]"))
#     )
#     time.sleep(3)
#     # Create a Select object
#     select = Select(dropdown_element)

#     # Select an option by visible text
#     select.select_by_visible_text("Mexico City")
#     print("Selected option by visible text: 'Mexico City'")

#     # # Select an option by value
#     # select.select_by_value("optionValue")
#     # print("Selected option by value: 'optionValue'")

#     # # Select an option by index
#     # select.select_by_index(2)
#     # print("Selected option by index: 2")

#     # Perform actions on the new tab
#     time.sleep(1)  # Just to observe the switch
#     # element = driver.find_element(By.TAG_NAME, "h1")
#     # print("Title on the new tab:", element.text)
#     print("---(2)---")
#     print(driver.current_url)

#     # Wait for a few seconds to see the new tab
#     time.sleep(2)

#     # Switch back to the original tab
#     driver.switch_to.window(driver.window_handles[0])

#     # Perform another action on the original tab (e.g., clicking a link from the search results)
#     first_result = driver.find_element(By.XPATH, "(//h3)[1]")

#     Inner_Text = first_result.get_attribute("innerText")

#     print("Inner text of the element is: ",Inner_Text)

#     try:
#         Is_enabled = first_result.is_enabled()

#         if Is_enabled:
#             print("The element is enabled")
#         else: 
#             print("The element is not enabled") 
#     finally:
#             first_result.click()

    

#     print("---(3)---")
#     print(driver.current_url)
#     # driver.back()
#     # driver.refresh()
#     # driver.forward()

#     # Wait for a few seconds to observe the click action
#     time.sleep(3)

# except Exception as e:
#     print(f"fail:{e}")

# finally:
#     # Close the browser
#     driver.quit()

