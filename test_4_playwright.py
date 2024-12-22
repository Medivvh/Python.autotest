from Pages.CheckoutComplite import CheckoutComplite
from Pages.CheckoutInfoPage import CheckoutInfoPage
from Pages.CheckoutStep2 import CheckoutStep2
from Pages.GoodsPage import GoodsPage
from Pages.LoginPage import LoginPage
from Pages.YourCartPage import YourCartPage
import pytest
from faker import Faker

faker = Faker()
FAKER = Faker(locale='en_US')

test_auth_params = dict(
    argnames='client',
    argvalues=['standard_user',
               'locked_out_user',
               'problem_user',
               'performance_glitch_user',
               'error_user',
               'visual_user'
               ]
)

name = faker.first_name()
secondname = faker.last_name()
postal = faker.postalcode()


@pytest.mark.parametrize(**test_auth_params)
def test_e2e(browser, client):
    page = browser.new_page()
    auth = LoginPage(page)
    goods = GoodsPage(page)
    cart = YourCartPage(page)
    check_1 = CheckoutInfoPage(page)
    check_2 = CheckoutStep2(page)
    check_executed = CheckoutComplite(page)

    auth.login(client, 'secret_sauce')
    goods.check_page()
    goods.add_red_switshot_good_in_cart()
    goods.add_Tshirt_in_cart()
    goods.remove_good_from_cart()
    goods.go_to_cart()
    cart.cart_have_good()
    cart.checkout()
    check_1.check_page()
    check_1.place_order(name, secondname, postal)
    check_2.finish_order()
    check_executed.check_main_elements()
    check_executed.check_burger_and_logout()


@pytest.mark.parametrize(**test_auth_params)
def test_auth(browser, client):
    page = browser.new_page()
    auth = LoginPage(page)
    auth.login(client, 'secret_sauce')
    pass


@pytest.mark.parametrize(**test_auth_params)
def test_check_goods(browser, client):
    page = browser.new_page()
    auth = LoginPage(page)
    auth.login(client, 'secret_sauce')
    goods = GoodsPage(page)
    goods.check_page()


@pytest.mark.parametrize(**test_auth_params)
def test_add_goods(browser, client):
    page = browser.new_page()
    auth = LoginPage(page)
    auth.login(client, 'secret_sauce')
    goods = GoodsPage(page)
    goods.take_goods_in_cart()
    goods.remove_goods()


@pytest.mark.parametrize(**test_auth_params)
def test_check_count_cart(browser, client):
    page = browser.new_page()
    auth = LoginPage(page)
    auth.login(client, 'secret_sauce')
    goods = GoodsPage(page)
    goods.add_random_good_in_cart_and_check_cart()


@pytest.mark.parametrize(**test_auth_params)
def test_check_goods_cart(browser, client):
    page = browser.new_page()
    auth = LoginPage(page)
    auth.login(client, 'secret_sauce')
    goods = GoodsPage(page)
    goods.add_random_good_in_cart()
    cart = YourCartPage(page)
    cart.cart_have_object()
    cart.checkout()


@pytest.mark.parametrize(**test_auth_params)
def test_empty_cart(browser, client):
    page = browser.new_page()
    auth = LoginPage(page)
    auth.login(client, 'secret_sauce')
    goods = GoodsPage(page)
    goods.add_random_good_in_cart_and_check_cart()
    cart = YourCartPage(page)
    cart.empty_cart()
    cart.checkout()
