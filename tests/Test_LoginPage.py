import pytest

from pages.ProductsPage import ProductsPage


class TestLoginPage:

    # Teste Atividade 01
    @pytest.mark.parametrize('all_browsers', ['chrome', 'firefox', 'edge'])
    def test_click_login_btn_validation(self, run_all_browsers, all_browsers):
        login_page = run_all_browsers
        login_page.click_login_btn()
        assert login_page.is_url_login(), "Página de login não foi encontrada!"
        assert login_page.has_login_error_message(), 'Nenhuma mensagem de erro foi encontrada'

    # Teste Atividade 02
    def test_validate_successful_login(self, setup):
        login_page = setup
        login_page.log_in_with_standard_user()
        product_page = ProductsPage(driver=login_page.driver)
        assert product_page.check_products_page(), "Login não foi realizado!"
