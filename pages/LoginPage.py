from selenium import webdriver
from selenium.webdriver.common.by import By


class LoginPage:
    # Locators

    url = 'https://www.saucedemo.com/'
    login_button = 'login-button'
    username_input = 'user-name'
    password_input = 'password'
    login_error_message = '.error-message-container'
    txt_login_error_message = 'Epic sadface: Username is required'
    standard_user = 'standard_user'
    password = 'secret_sauce'

    # Services

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get(self.url)

    def close(self):
        self.driver.quit()

    def click_login_btn(self):
        self.driver.find_element(By.ID, self.login_button).click()

    def log_in_with_standard_user(self):
        self.driver.find_element(By.ID, self.username_input).send_keys(self.standard_user)
        self.driver.find_element(By.ID, self.password_input).send_keys(self.password)
        self.click_login_btn()

    def is_url_login(self):
        return self.driver.current_url == self.url

    def has_login_error_message(self):
        error_message = self.driver.find_element(By.CSS_SELECTOR, self.login_error_message).text
        return error_message == self.txt_login_error_message
