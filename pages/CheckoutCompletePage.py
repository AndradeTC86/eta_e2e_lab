from selenium.webdriver.common.by import By

from pages.PageObject import PageObject


class CheckoutCompletePage(PageObject):
    # Locators

    url = 'https://www.saucedemo.com/checkout-complete.html'
    page_title = 'Checkout: Complete!'
    class_complete_header = 'complete-header'
    txt_complete_header = 'Thank you for your order!'

    # Services
    def __init__(self, driver=None):
        super(CheckoutCompletePage, self).__init__(driver)

    def check_checkout_complete_page(self):
        return self.check_page(self.url, self.page_title)

    def validate_order_message(self):
        return self.driver.find_element(By.CLASS_NAME, self.class_complete_header).text == self.txt_complete_header
