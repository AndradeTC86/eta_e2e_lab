from random import randint
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from pages.PageObject import PageObject


class ProductsPage(PageObject):
    # Locators

    url = 'https://www.saucedemo.com/inventory.html'
    page_title = 'Products'
    product_list = 'inventory_item'
    btn_add_to_cart = 'btn_primary'
    btn_remove_from_cart = 'btn_secondary'
    class_cart_badge = 'shopping_cart_badge'
    class_cart_btn = 'shopping_cart_link'
    class_inventory_item_name = 'inventory_item_name'
    text_remove_btn = 'Remove'
    css_sort_menu = '[data-test="product_sort_container"]'
    css_sort_option_low_to_high = '[value="lohi"]'
    css_sort_option_high_to_low = '[value="hilo"]'
    css_sort_option_z_to_a = '[value="za"]'
    class_inventory_item_price = 'inventory_item_price'

    # Services

    def __init__(self, driver):
        super(ProductsPage, self).__init__(driver=driver)

    def check_products_page(self):
        return self.check_page(self.url, self.page_title)

    def get_product_list_size(self):
        product_list = self.driver.find_elements(By.CLASS_NAME, self.product_list)
        return len(product_list)

    def add_random_product_to_cart(self):
        product_list = self.driver.find_elements(By.CLASS_NAME, self.product_list)
        random_product = randint(0, len(product_list) -1)
        product_element = product_list[random_product]
        product_element.find_element(By.CLASS_NAME, self.btn_add_to_cart).click()
        remove_btn_text = product_element.find_element(By.CLASS_NAME, self.btn_remove_from_cart).text
        if remove_btn_text != self.text_remove_btn:
            raise Exception('Botão para remover não foi encontrado')
        return product_element.find_element(By.CLASS_NAME, self.class_inventory_item_name).text

    def get_cart_badge_number(self):
        return self.driver.find_element(By.CLASS_NAME, self.class_cart_badge).text

    def click_cart_btn(self):
        self.driver.find_element(By.CLASS_NAME, self.class_cart_btn).click()

    def sort_products_from_low_to_high(self):
        self.driver.find_element(By.CSS_SELECTOR, self.css_sort_menu).click()
        self.driver.find_element(By.CSS_SELECTOR, self.css_sort_option_low_to_high).click()

    def validate_sorted_products_low_to_high(self):
        all_price_items = self.driver.find_elements(By.CLASS_NAME, self.class_inventory_item_price)
        for i in range(len(all_price_items)-1):
            current_price = float(all_price_items[i].text.replace('$', ''))
            print(f'Current price:{current_price}')
            next_price = float(all_price_items[i+1].text.replace('$', ''))
            print(f'Next price:{next_price}')
            if current_price > next_price:
                return False
        return True

    def sort_products_from_high_to_low(self):
        self.driver.find_element(By.CSS_SELECTOR, self.css_sort_menu).click()
        self.driver.find_element(By.CSS_SELECTOR, self.css_sort_option_high_to_low).click()

    def validate_sorted_products_high_to_low(self):
        all_price_items = self.driver.find_elements(By.CLASS_NAME, self.class_inventory_item_price)
        for i in range(len(all_price_items)-1):
            current_price = float(all_price_items[i].text.replace('$', ''))
            print(f'Current price:{current_price}')
            next_price = float(all_price_items[i+1].text.replace('$', ''))
            print(f'Next price:{next_price}')
            if current_price < next_price:
                return False
        return True

    def sort_products_from_z_to_a(self):
        self.driver.find_element(By.CSS_SELECTOR, self.css_sort_menu).click()
        self.driver.find_element(By.CSS_SELECTOR, self.css_sort_option_z_to_a).click()

    def validate_sorted_products_z_to_a(self):
        all_title_items = self.driver.find_elements(By.CLASS_NAME, self.class_inventory_item_name)
        for i in range(len(all_title_items)-1):
            current_name = all_title_items[i].text
            print(f'Current name:{current_name}')
            next_name = all_title_items[i+1].text
            print(f'Next name:{next_name}')
            if current_name < next_name:
                return False
        return True

    def validate_default_products_sorted_a_to_z(self):
        all_title_items = self.driver.find_elements(By.CLASS_NAME, self.class_inventory_item_name)
        for i in range(len(all_title_items)-1):
            current_name = all_title_items[i].text
            print(f'Current name:{current_name}')
            next_name = all_title_items[i+1].text
            print(f'Next name:{next_name}')
            if current_name > next_name:
                return False
        return True







