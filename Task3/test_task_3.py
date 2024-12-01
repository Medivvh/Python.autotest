import pytest

from conftest import booking_data
from constant import BASE_URL
from assertpy import assert_that

test_auth_params = dict(
    argnames='test_type',
    argvalues=['token', 'header']
)


class TestBookings:

    @pytest.mark.parametrize(**test_auth_params)
    def test_create_booking(self, booking_data, auth_session, test_type, auth_session_with_basic):
        data = booking_data()
        if test_type == 'token':
            create_booking = auth_session.post(f"{BASE_URL}/booking", json=data)
        else:
            create_booking = auth_session_with_basic.post(f"{BASE_URL}/booking", json=data)

        assert_that(create_booking.status_code).is_equal_to(200)

        booking_id = create_booking.json().get("bookingid")
        assert_that(booking_id).is_not_equal_to(None)

        get_booking = auth_session.get(f"{BASE_URL}/booking/{booking_id}")
        assert_that(get_booking.status_code).is_equal_to(200)

        booking_data_response = get_booking.json()
        assert_that(booking_data_response).is_equal_to(data)

        delete_booking = auth_session.delete(f"{BASE_URL}/booking/{booking_id}")
        assert_that(delete_booking.status_code).is_equal_to(201)

        get_deleted_booking = auth_session.get(f"{BASE_URL}/booking/{booking_id}")
        assert_that(get_deleted_booking.status_code).is_equal_to(404)

    @pytest.mark.parametrize(**test_auth_params)
    def test_update_booking(self, booking_data, auth_session, booking, test_type, auth_session_with_basic):
        booking_id, old_person = booking()
        new_person = booking_data()
        if test_type == 'token':
            update_booking = auth_session.put(f"{BASE_URL}/booking/{booking_id}", json=new_person)
        else:
            update_booking = auth_session_with_basic.put(f"{BASE_URL}/booking/{booking_id}", json=new_person)
        assert_that(update_booking.status_code).is_equal_to(200)
        assert_that(old_person).is_not_equal_to(update_booking.json())

    def test_get_booking(self, auth_session, booking_data, booking, get_booking_ids):
        booking_id, data_booking = booking()
        list_of_ids = get_booking_ids()
        assert_that(list_of_ids).contains({'bookingid': booking_id})

    def test_get_booking_by_url(self, booking_data, booking, auth_session):
        booking_id, data_booking = booking()
        get_booking_by_url = auth_session.get(
            f'{BASE_URL}/booking',
            params={
                'firstname': data_booking['firstname'],
                'lastname': data_booking['lastname']
            }
        )
        assert_that(get_booking_by_url.status_code).is_equal_to(200), 'Не найден созданный клиент'

    @pytest.mark.parametrize(**test_auth_params)
    def test_patch_booking(self, booking_data, auth_session, booking, test_type, auth_session_with_basic):
        booking_id, data_booking = booking()
        if test_type == 'token':
            update_booking = auth_session.patch(f"{BASE_URL}/booking/{booking_id}", json={'firstname': 'IRINA'})
        else:
            update_booking = auth_session.patch(f"{BASE_URL}/booking/{booking_id}", json={'firstname': 'NINA'})

        assert_that(update_booking.status_code).is_equal_to(200), 'Unavailable status code'
        new_person = update_booking.json()
        assert_that(new_person['firstname']).is_not_equal_to(data_booking['firstname']), 'Имена совпадают'
        del new_person['firstname']
        del data_booking['firstname']
        assert_that(new_person).is_equal_to(data_booking), 'Пользователи не равны'


class Test_negative_booking:
    def test_unavailable_data(self, auth_session, booking_data, booking):
        booking_id, old_person = booking()
        data = booking_data()
        update_wrong_data = data['depositpaid'] = None
        update_wrong_booking = auth_session.put(f"{BASE_URL}/booking/{booking_id}", json=update_wrong_data)
        assert_that(update_wrong_booking.status_code).is_equal_to(400), 'Приняты невалидные значения'

    def test_update_booking(self, booking_data, booking, auth_session_with_basic):
        booking_id, old_person = booking()
        data = booking_data()
        auth_session_with_basic.headers.update({"Authorization": None})
        update_booking = auth_session_with_basic.put(f"{BASE_URL}/booking/{booking_id}", json=data)
        assert_that(update_booking.status_code).is_equal_to(403), 'Нет ошибки Forbidden'

    def test_get_booking(self, auth_session, booking_data, get_booking_ids):
        get_booking_id = auth_session.get(f'{BASE_URL}/boоking')  # в методе используется кириллица
        assert_that(get_booking_id.status_code).is_equal_to(404), 'Ошибка. В латиннице есть кириллица'

    def test_update_zero(self, auth_session, booking_data):
        get_booking = auth_session.get(f"{BASE_URL}/booking/0")
        assert_that(get_booking.status_code).is_equal_to(404), 'Найден существующий id'
        update_data = booking_data()
        update_booking = auth_session.put(f"{BASE_URL}/booking/0", json=update_data)
        assert_that(update_booking.status_code).is_equal_to(405), 'Изменен несуществующий id'
