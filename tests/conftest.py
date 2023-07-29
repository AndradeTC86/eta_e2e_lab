import pytest

from pages.LoginPage import LoginPage
from pages.ProductsPage import ProductsPage


def pytest_addoption(parser):
    parser.addoption("--browser", default="chrome", help="Selecione o seu browser")


@pytest.fixture
def select_browser(request):
    yield request.config.getoption("--browser").lower()


@pytest.fixture
def setup(select_browser):
    login_page = LoginPage(browser=select_browser)
    yield login_page
    login_page.close()


@pytest.fixture
def run_all_browsers(all_browsers):
    login_page = LoginPage(browser=all_browsers)
    yield login_page
    login_page.close()


@pytest.fixture()
def login_saucedemo(setup):
    login_page = setup
    login_page.log_in_with_standard_user()
    yield login_page


@pytest.fixture
def has_product_in_cart(login_saucedemo):
    product_page = ProductsPage(driver=login_saucedemo.driver)
    product_name = product_page.add_random_product_to_cart()
    assert product_page.get_cart_badge_number() == '1', 'Quantidade de produtos no carrinho está incorreta'
    yield product_page, product_name
