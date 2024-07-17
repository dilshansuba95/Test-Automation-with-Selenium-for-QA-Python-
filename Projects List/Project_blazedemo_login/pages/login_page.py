from selenium.webdriver.common.by import By

#page object model for the login page
class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.email_input = (By.ID, "email")
        self.password_input = (By.ID, "password")
        self.remember_me_checkbox = (By.ID, "remember_me")
        self.login_button = (By.ID, "login_button")
        self.error_message = (By.ID, "error_message")

    def enter_email(self, email):
        self.driver.find_element(*self.email_input).send_keys(email)

    def enter_password(self, password):
        self.driver.find_element(*self.password_input).send_keys(password)

    def click_remember_me(self):
        self.driver.find_element(*self.remember_me_checkbox).click()

    def click_login(self):
        self.driver.find_element(*self.login_button).click()

    def get_error_message(self):
        return self.driver.find_element(*self.error_message).text