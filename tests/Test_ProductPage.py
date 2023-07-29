import time

from pages.CartPage import CartPage
from pages.ProductsPage import ProductsPage


class TestProductPage:

    # Teste Atividade 06
    def test_add_product_in_cart(self, has_product_in_cart):
        product_page, product_name = has_product_in_cart
        product_page.click_cart_btn()
        cart_page = CartPage(product_page.driver)
        assert cart_page.check_product_information(product_name), "Informações do produto estão incorretas"

    # Teste Atividade 07a
    def test_filter_products_by_price_low_to_high(self, login_saucedemo):
        product_page = ProductsPage(driver=login_saucedemo.driver)
        assert product_page.check_products_page(), "Página de produtos não foi encontrada!"
        assert product_page.get_product_list_size() > 0, 'Lista de produtos está vazia!'
        product_page.sort_products_from_low_to_high()
        assert product_page.validate_sorted_products_low_to_high(), "Ordem dos produtos está incorreta"

    # Teste Atividade 07b
    def test_filter_products_by_price_high_to_low(self, login_saucedemo):
        product_page = ProductsPage(driver=login_saucedemo.driver)
        assert product_page.check_products_page(), "Página de produtos não foi encontrada!"
        assert product_page.get_product_list_size() > 0, 'Lista de produtos está vazia!'
        product_page.sort_products_from_high_to_low()
        assert product_page.validate_sorted_products_high_to_low(), "Ordem dos produtos está incorreta"

    # Teste Atividade 07c
    def test_filter_products_by_price_z_to_a(self, login_saucedemo):
        product_page = ProductsPage(driver=login_saucedemo.driver)
        assert product_page.check_products_page(), "Página de produtos não foi encontrada!"
        assert product_page.get_product_list_size() > 0, 'Lista de produtos está vazia!'
        product_page.sort_products_from_z_to_a()
        assert product_page.validate_sorted_products_z_to_a(), "Ordem dos produtos está incorreta"

