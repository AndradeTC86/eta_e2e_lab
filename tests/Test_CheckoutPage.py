import pytest

from pages.CartPage import CartPage
from pages.CheckoutCompletePage import CheckoutCompletePage
from pages.CheckoutInfoPage import CheckoutInfoPage
from pages.CheckoutOverviewPage import CheckoutOverviewPage


class TestCheckout:

    # Teste Atividade 04
    def test_verify_error_message_in_checkout(self, has_product_in_cart):
        product_page, product_name = has_product_in_cart
        product_page.click_cart_btn()
        cart_page = CartPage(driver=product_page.driver)
        assert cart_page.check_your_cart_page(), 'Página do carrinho não foi encontrada'
        cart_page.click_btn_checkout()
        checkout_page = CheckoutInfoPage(driver=cart_page.driver)
        assert checkout_page.check_checkout_info_page(), "Página de checkout info não foi encontrada"
        checkout_page.click_btn_continue()
        assert checkout_page.validate_first_name_required_error_message(), 'Nenhuma mensagem de erro foi encontrada'

    # Teste Atividade 05
    @pytest.mark.parametrize('select_browser', ['firefox'])
    def test_complete_order(self, has_product_in_cart, select_browser):
        product_page, product_name = has_product_in_cart
        product_page.click_cart_btn()
        cart_page = CartPage(driver=product_page.driver)
        cart_page.click_btn_checkout()
        checkout_page = CheckoutInfoPage(driver=cart_page.driver)
        checkout_page.submit_order_info()
        overview_page = CheckoutOverviewPage(driver=checkout_page.driver)
        assert overview_page.check_checkout_overview_page(), "Página de checkout overview não foi encontrada"
        assert overview_page.check_product_information(product_name), "Informações do produto estão incorretas"
        overview_page.click_btn_finish()
        complete_page = CheckoutCompletePage(driver=overview_page.driver)
        assert complete_page.check_checkout_complete_page(), "Página de checkout overview não foi encontrada"
        assert complete_page.validate_order_message(), "Mensagem de sucesso não foi encontrada"
