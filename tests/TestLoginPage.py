from pages.ProductsPage import ProductsPage


class TestLoginPage:

    def test_click_login_btn_validation(self, setup):
        login_page = setup
        login_page.click_login_btn()

        assert login_page.is_url_login(), "Página incorreta!"
        assert login_page.has_login_error_message(), 'Nenhuma mensagem de erro foi encontrada'

    def test_validate_successful_login(self, setup):
        login_page = setup
        login_page.log_in_with_standard_user()
        product_page = ProductsPage(driver=login_page.driver)

        assert product_page.is_url_products(), "Login não foi realizado!"
        assert product_page.has_products_title(), 'Título diferente do esperado!'
        assert product_page.get_product_list_size() > 0, 'Lista de produtos está vazia!'
