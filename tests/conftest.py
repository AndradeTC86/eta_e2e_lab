import pytest

from pages.LoginPage import LoginPage
from pages.ProductsPage import ProductsPage


@pytest.fixture
def setup():
    login_page = LoginPage()
    yield login_page
    login_page.close()

@pytest.fixture()
def login_saucedemo(setup):
    login_page = setup
    login_page.log_in_with_standard_user()
    yield login_page
