from selenium.webdriver.common.by import By
from pages.PageObject import PageObject


class MenuPage(PageObject):

    # Locators

    menu_burger = 'react-burger-menu-btn'
    logout_menu_item = 'logout_sidebar_link'

    # Services

    def __init__(self, driver=None):
        super(MenuPage, self).__init__(driver)

    def click_burger_menu(self):
        self.driver.find_element(By.ID, self.menu_burger).click()

    def click_logout_link(self):
        self.click_burger_menu()
        self.driver.find_element(By.ID, self.logout_menu_item).click()
