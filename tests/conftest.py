import pytest

from pages.LoginPage import LoginPage
from pages.ProductsPage import ProductsPage


@pytest.fixture
def setup():
    login_page = LoginPage()
    yield login_page
    login_page.close()