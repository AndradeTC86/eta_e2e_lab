from selenium import webdriver
from selenium.webdriver.common.by import By


class PageObject:

    # Locators

    menu_burger = 'react-burger-menu-btn'
    logout_link = 'logout_sidebar_link'

    # Services

    def __init__(self, driver=None):
        if driver:
            self.driver = driver
        else:
            self.driver = webdriver.Chrome()
            self.driver.maximize_window()

    def close(self):
        self.driver.quit()

    def click_burger_menu(self):
        self.driver.find_element(By.ID, self.menu_burger).click()

    def click_logout_link(self):
        self.click_burger_menu()
        self.driver.implicitly_wait(1)
        self.driver.find_element(By.ID, self.logout_link).click()
