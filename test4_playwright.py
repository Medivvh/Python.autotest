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
    argvalues=[1, 2, 3, 4, 5, 6]
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
    if client == 1:
        auth.login('standard_user', 'secret_sauce')
    elif client == 2:
        auth.login('locked_out_user', 'secret_sauce')
    elif client == 3:
        auth.login('problem_user', 'secret_sauce')
    elif client == 4:
        auth.login('performance_glitch_user', 'secret_sauce')
    elif client == 5:
        auth.login('error_user', 'secret_sauce')
    else:
        auth.login('visual_user', 'secret_sauce')

    goods.check_page()
    goods.add_first_good_in_cart()
    goods.add_second_good_in_cart()
    goods.remove_good_from_cart()
    goods.go_to_cart()
    cart.cart_have_good()
    cart.checkout()
    check_1.check_page()
    check_1.place_order(name, secondname, postal)
    check_2.finish_order()
    check_executed.check_main_elements()
    check_executed.check_burger_and_logout()
