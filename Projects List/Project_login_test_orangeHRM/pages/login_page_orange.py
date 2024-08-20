from selenium.webdriver.common.by import By
import time

class LoginPage_orange():
    def __init__ (self, driver):
        self.driver = driver
        self.username_input = (By.XPATH,"//*[@id=\"app\"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input")
        self.password_input = (By.XPATH,"//*[@id=\"app\"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input")
        self.login_button = (By.XPATH,"//*[@id=\"app\"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button")
        self.error_msg = (By.XPATH,"//*[@id=\"app\"]/div[1]/div/div[1]/div/div[2]/div[2]/div/div/div[1]/p")
        self.username_error = (By.XPATH,"//*[@id=\"app\"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/span")
        self.password_error = (By.XPATH,"//*[@id=\"app\"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/span")

    def enter_username(self, username):  
        self.driver.find_element(*self.username_input).send_keys(username)
        time.sleep(1)

    def enter_empty_username(self):  
        self.driver.find_element(*self.username_input).clear()
        time.sleep(1)

    def enter_password(self, password):
        self.driver.find_element(*self.password_input).send_keys(password)
        time.sleep(1)

    def enter_empty_password(self):
        self.driver.find_element(*self.password_input).clear()
        time.sleep(1)

    def click_login_button(self):
        self.driver.find_element(*self.login_button).click()
        time.sleep(6)
        
    def get_error_msg(self):
        return self.driver.find_element(*self.error_msg).text
    
    def get_empty_username_error_msg(self):
        return self.driver.find_element(*self.username_error).text
    
    def get_empty_password_error_msg(self):
        return self.driver.find_element(*self.password_error).text
    
    
