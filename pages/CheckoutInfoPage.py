from selenium.webdriver.common.by import By
from pages.PageObject import PageObject


class CheckoutInfoPage(PageObject):
    # Locators
    id_btn_continue = 'continue'
    class_error_message = 'error-message-container'
    txt_class_first_name_error_message = 'Error: First Name is required'
    url = 'https://www.saucedemo.com/checkout-step-one.html'
    page_title = 'Checkout: Your Information'
    id_first_name_input = 'first-name'
    id_last_name_input = 'last-name'
    id_postal_code_input = 'postal-code'
    first_name = 'Cliente'
    last_name = 'Teste'
    postal_code = '00000000'

    # Services
    def __init__(self, driver=None):
        super(CheckoutInfoPage, self).__init__(driver)

    def click_btn_continue(self):
        self.driver.find_element(By.ID, self.id_btn_continue).click()

    def check_checkout_info_page(self):
        return self.check_page(self.url, self.page_title)

    def validate_first_name_required_error_message(self):
        error_message = self.driver.find_element(By.CLASS_NAME, self.class_error_message).text
        return error_message == self.txt_class_first_name_error_message

    def submit_order_info(self):
        self.driver.find_element(By.ID, self.id_first_name_input).send_keys(self.first_name)
        self.driver.find_element(By.ID, self.id_last_name_input).send_keys(self.last_name)
        self.driver.find_element(By.ID, self.id_postal_code_input).send_keys(self.postal_code)
        self.click_btn_continue()
