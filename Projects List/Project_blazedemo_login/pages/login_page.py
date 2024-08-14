from selenium.webdriver.common.by import By
import time

#page object model for the login page
class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.email_input = (By.ID, "email")
        self.password_input = (By.ID, "password")
        self.remember_me_checkbox = (By.XPATH, '//*[@id="app"]/div/div/div/div/div[2]/form/div[3]/div/div/label/input')
        self.login_button = (By.CSS_SELECTOR, "button[type='submit']")
        self.error_message = (By.CSS_SELECTOR, "body > div > div.message")

    def enter_email(self, email):
        # Implement logic to enter email
        self.driver.find_element(*self.email_input).send_keys(email)

    def enter_password(self, password):
        # Implement logic to enter password
        self.driver.find_element(*self.password_input).send_keys(password)

    def click_remember_me(self):
        # Implement logic to click remember me checkbox
        self.driver.find_element(*self.remember_me_checkbox).click()

    def click_login(self):
        # Implement logic to click the login button
        self.driver.find_element(*self.login_button).click()
        time.sleep(4)

    def get_error_message(self):
        # Implement logic to retrieve error message
        return self.driver.find_element(*self.error_message).text