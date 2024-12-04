from Pages.CheckoutComplite import CheckoutComplite
from Pages.CheckoutInfoPage import CheckoutInfoPage
from Pages.CheckoutStep2 import CheckoutStep2
from Pages.GoodsPage import GoodsPage
from Pages.LoginPage import LoginPage
from Pages.YourCartPage import YourCartPage


def test_e2e(browser):
    page = browser.new_page()
    auth = LoginPage(page)
    goods = GoodsPage(page)
    cart = YourCartPage(page)
    check_1 = CheckoutInfoPage(page)
    check_2 = CheckoutStep2(page)
    check_executed = CheckoutComplite(page)

    auth.login('standard_user', 'secret_sauce')
    goods.check_page()
    goods.add_first_good_in_cart()
    goods.add_second_good_in_cart()
    goods.remove_good_from_cart()
    goods.go_to_cart()
    cart.cart_have_good()
    cart.checkout()
    check_1.check_page()
    check_1.place_order('Andrew', 'Volina', '12441')
    check_2.finish_order()
    check_executed.check_main_elements()
    check_executed.check_burger_and_logout()


def test_negative(browser):
    page = browser.new_page()
    auth = LoginPage(page)
    goods = GoodsPage(page)

    auth.login('problem_user', 'secret_sauce')
    goods.check_page()
