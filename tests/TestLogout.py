class TestLogout:

    def test_logout(self, setup):
        login_page = setup
        login_page.log_in_with_standard_user()
        login_page.click_logout_link()

        assert login_page.is_url_login(), "Página incorreta!"
