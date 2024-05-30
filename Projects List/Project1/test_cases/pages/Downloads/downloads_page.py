from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def click_download_python(driver , python_version):
    wait = WebDriverWait(driver, 30)
    download_python_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id=\"touchnav-wrapper\"]/header/div/div[2]/div/div[2]/p/a")))
    print('~~~~~~~~~~~~~~~~')
    print(download_python_button.text)
    if python_version == download_python_button.text :
        print('Test Case Passed')
    else:
        print('Test Case Failed. The version avaialable to download is'+ download_python_button.text)
    return driver


