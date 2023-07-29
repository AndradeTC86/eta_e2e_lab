from selenium.webdriver.common.by import By
from pages.PageObject import PageObject


class CheckoutOverviewPage(PageObject):
    # Locators

    url = 'https://www.saucedemo.com/checkout-step-two.html'
    page_title = 'Checkout: Overview'
    id_btn_finish = 'finish'
    class_inventory_item_name = 'inventory_item_name'

    # Services
    def __init__(self, driver=None):
        super(CheckoutOverviewPage, self).__init__(driver)

    def check_checkout_overview_page(self):
        return self.check_page(self.url, self.page_title)

    def check_product_information(self, product_name):
        return self.driver.find_element(By.CLASS_NAME, self.class_inventory_item_name).text == product_name

    def click_btn_finish(self):
        self.driver.find_element(By.ID, self.id_btn_finish).click()

