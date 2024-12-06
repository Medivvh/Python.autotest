import pytest
import requests
import random

from assertpy import assert_that
from faker import Faker

from constant import HEADERS, BASE_URL
from playwright.sync_api import sync_playwright

faker = Faker()
FAKER = Faker(locale='en_US')


@pytest.fixture(scope="session")
def auth_session():
    """Создаёт сессию с авторизацией и возвращает объект сессии."""
    session = requests.Session()
    session.headers.update(HEADERS)

    auth_response = session.post(f"{BASE_URL}/auth", json={"username": "admin", "password": "password123"})
    assert_that(auth_response.status_code).is_equal_to(200), "Ошибка авторизации, статус код не 200"
    token = auth_response.json().get("token")
    assert_that(token).is_not_none(), "Токен не найден в ответе"

    session.headers.update({"Cookie": f"token={token}"})
    return session


@pytest.fixture(scope="session")
def auth_session_with_basic():
    """Создаёт сессию с авторизацией c хедером Authorization."""
    session = requests.Session()
    session.headers.update(HEADERS)

    auth_response = session.post(f"{BASE_URL}/auth", json={"username": "admin", "password": "password123"})
    assert_that(auth_response.status_code).is_equal_to(200), "Ошибка авторизации, статус код не 200"
    basic = "Basic YWRtaW46cGFzc3dvcmQxMjM="
    session.headers.update({"Authorization": f"{basic}"})
    return session


@pytest.fixture()
def booking_data():
    def _booking_data():
        return {
            "firstname": faker.first_name(),
            "lastname": faker.last_name(),
            "totalprice": faker.random_int(min=100, max=10000),
            "depositpaid": random.choice([True, False]),
            "bookingdates": {
                "checkin": faker.date(),
                "checkout": faker.date()
            },
            "additionalneeds": faker.pystr()
        }

    return _booking_data


@pytest.fixture()
def booking(booking_data, auth_session):
    booking_id = None

    def _create_booking():
        nonlocal booking_id
        data_of_booking = booking_data()
        create_booking = auth_session.post(f"{BASE_URL}/booking", json=data_of_booking)
        assert_that(create_booking.status_code).is_equal_to(200)
        booking_id = create_booking.json().get("bookingid")
        return booking_id, data_of_booking

    yield _create_booking

    remove = auth_session.delete(f"{BASE_URL}/booking/{booking_id}")
    assert_that(remove.status_code).is_equal_to(201)

    get_deleted_booking = auth_session.get(f"{BASE_URL}/booking/{booking_id}")
    assert_that(get_deleted_booking.status_code).is_equal_to(404)


@pytest.fixture()
def get_booking_ids(auth_session):
    def _get_booking():
        get_booking_id = auth_session.get(f'{BASE_URL}/booking')
        assert_that(get_booking_id.status_code).is_equal_to(200) and get_booking_id is not None
        list_of_id = get_booking_id.json()
        return list_of_id

    return _get_booking


@pytest.fixture(scope='session')
def browser():
    playwright = sync_playwright().start()
    browser = playwright.chromium.launch(headless=False, slow_mo=1200)
    yield browser
    browser.close()
    playwright.stop()

# @pytest.fixture(scope='session')
# def e2e(browser):
#     page = browser.new_page()
#     auth = LoginPage(page)
#     goods = GoodsPage(page)
#     cart = YourCartPage(page)
#     check_1 = CheckoutInfoPage(page)
#     check_2 = CheckoutStep2(page)
#     check_executed = CheckoutComplite(page)
#
#     auth.login('standard_user', 'secret_sauce')
#     goods.check_page()
#     goods.add_first_good_in_cart()
#     goods.add_second_good_in_cart()
#     goods.remove_good_from_cart()
#     goods.go_to_cart()
#     cart.cart_have_good()
#     cart.checkout()
#     check_1.check_page()
#     check_1.place_order('Andrew', 'Volina', '12441')
#     check_2.finish_order()
#     check_executed.check_main_elements()
#     check_executed.check_burger_and_logout()
