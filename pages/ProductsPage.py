from selenium.webdriver.common.by import By

from pages.PageObject import PageObject


class ProductsPage(PageObject):
    # Locators

    url = 'https://www.saucedemo.com/inventory.html'
    inventory_page_title = 'title'
    inventory_page_title_text = 'Products'
    product_list = 'inventory_item'

    # Services

    def __init__(self, driver):
        super(ProductsPage, self).__init__(driver=driver)

    def is_url_products(self):
        return self.driver.current_url == self.url

    def has_products_title(self):
        page_title = self.driver.find_element(By.CLASS_NAME, self.inventory_page_title).text
        return page_title == self.inventory_page_title_text

    def get_product_list_size(self):
        product_list = self.driver.find_elements(By.CLASS_NAME, self.product_list)
        return len(product_list)
