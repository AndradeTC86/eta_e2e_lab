from selenium.webdriver.common.by import By
from pages.PageObject import PageObject


class CartPage(PageObject):
    # Locators

    id_checkout_btn = 'checkout'
    url = 'https://www.saucedemo.com/cart.html'
    page_title = 'Your Cart'
    class_inventory_item_name = 'inventory_item_name'

    # Services
    def __init__(self, driver=None):
        super(CartPage, self).__init__(driver)

    def check_your_cart_page(self):
        return self.check_page(self.url, self.page_title)

    def click_btn_checkout(self):
        self.driver.find_element(By.ID, self.id_checkout_btn).click()

    def check_product_information(self, product_name):
        return self.driver.find_element(By.CLASS_NAME, self.class_inventory_item_name).text == product_name



