
import pytest
import requests
from faker import Faker
from constant import HEADERS, BASE_URL
from requests import session

faker = Faker()
FAKER = Faker(locale='en_US')


@pytest.fixture(scope="session")
def auth_session():
    """Создаёт сессию с авторизацией и возвращает объект сессии."""
    session = requests.Session()
    session.headers.update(HEADERS)

    auth_response = session.post(f"{BASE_URL}/auth", json={"username": "admin", "password": "password123"})
    assert auth_response.status_code == 200, "Ошибка авторизации, статус код не 200"
    token = auth_response.json().get("token")
    assert token is not None, "Токен не найден в ответе"

    session.headers.update({"Cookie": f"token={token}"})
    return session

@pytest.fixture()
def booking_data():
    return {
        "firstname": faker.first_name(),
        "lastname": faker.last_name(),
        "totalprice": faker.random_int(min=100, max=10000),
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2024-04-05",
            "checkout": "2024-04-08"
        },
        "additionalneeds": "Breakfast"
        }

@pytest.fixture()
def update_data():
    return {
        "firstname": faker.first_name(),
        "lastname": faker.last_name(),
        "totalprice": faker.random_int(min=100, max=10000),
        "depositpaid": False,
        "bookingdates": {
            "checkin": "2024-11-20",
            "checkout": "2024-11-20"
        },
        "additionalneeds": "sleep"

        }

@pytest.fixture(scope="session")
def auth_session_with_basic():
    """Создаёт сессию с авторизацией c хедером Authorization."""
    session = requests.Session()
    session.headers.update(HEADERS)

    auth_response = session.post(f"{BASE_URL}/auth", json={"username": "admin", "password": "password123"})
    assert auth_response.status_code == 200, "Ошибка авторизации, статус код не 200"
    basic = "Basic YWRtaW46cGFzc3dvcmQxMjM="
    session.headers.update({"Authorization": f"{basic}"})
    return session

@pytest.fixture(scope='session')
def create_random_id():
    random_id = {"bookingid": faker.random_int(min=1, max=10000)}
    return random_id


@pytest.fixture()
def create_zero_id():
    zero_client = {"bookingid": 0}
    return zero_client

@pytest.fixture()
def update_wrong_data():
    return {
        "firstname": faker.first_name(),
        "lastname": faker.last_name(),
        "totalprice": faker.random_int(min=100, max=10000),
        "depositpaid": "True",
        "bookingdates": {
            "checkin": "2024-11-20",
            "checkout": "2024-11-20"
        },
        "additionalneeds": "sleep"

        }


