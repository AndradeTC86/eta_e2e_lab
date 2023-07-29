from pages.MenuPage import MenuPage


class TestLogout:

    # Teste Atividade 03
    def test_logout(self, login_saucedemo):
        menu_page = MenuPage(driver=login_saucedemo.driver)
        menu_page.click_logout_link()
        assert login_saucedemo.is_url_login(), "Página incorreta!"
