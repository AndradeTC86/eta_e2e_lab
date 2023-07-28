from pages.MenuPage import MenuPage


class TestLogout:

    def test_logout(self, login_saucedemo):
        menu = MenuPage(driver=login_saucedemo.driver)
        menu.click_logout_link()

        assert login_saucedemo.is_url_login(), "Página incorreta!"
