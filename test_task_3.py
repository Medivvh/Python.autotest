import pytest
import requests
from functools import reduce
from conftest import update_data, booking_data
from constant import BASE_URL



class TestBookings:

    def test_create_booking(self, booking_data, auth_session):
        create_booking = auth_session.post(f"{BASE_URL}/booking", json = booking_data)
        assert create_booking.status_code == 200
        booking_id = create_booking.json().get("bookingid")
        assert booking_id is not None, "ID букинга не найден в ответе"

        get_booking = auth_session.get(f"{BASE_URL}/booking/{booking_id}")
        assert get_booking.status_code == 200

        booking_data_response = get_booking.json()
        assert booking_data_response['firstname'] == booking_data['firstname'], "Имя не совпадает с заданным"
        assert booking_data_response['lastname'] == booking_data['lastname'], "Фамилия не совпадает с заданной"
        assert booking_data_response['totalprice'] == booking_data['totalprice'], "Цена не совпадает с заданной"
        assert booking_data_response['depositpaid'] == booking_data['depositpaid'], "Статус депозита не совпадает"
        assert booking_data_response['bookingdates']['checkin'] == booking_data['bookingdates'][
            'checkin'], "Дата заезда не совпадает"
        assert booking_data_response['bookingdates']['checkout'] == booking_data['bookingdates'][
            'checkout'], "Дата выезда не совпадает"

        delete_booking = auth_session.delete(f"{BASE_URL}/booking/{booking_id}")
        assert delete_booking.status_code == 201, f"Ошибка при удалении букинга с ID {booking_id}"

        get_deleted_booking = auth_session.get(f"{BASE_URL}/booking/{booking_id}")
        assert get_deleted_booking.status_code == 404, "Букинг не был удален"


    def test_update_booking(self, booking_data, auth_session, update_data):
        create_booking = auth_session.post(f"{BASE_URL}/booking", json=booking_data)
        booking_id = create_booking.json().get("bookingid")
        old_person = create_booking.json()['booking']
        update_booking = auth_session.put(f"{BASE_URL}/booking/{booking_id}", json = update_data)
        assert update_booking.status_code == 200, 'Unavailable status code'
        new_person = update_booking.json()
        assert new_person['firstname'] != old_person['firstname'], 'Имена совпадают'
        assert new_person['lastname'] != old_person['lastname'], 'Фамилии совпадают'
        assert new_person['totalprice'] != old_person['totalprice'], 'Суммы совпадают'
        assert new_person['depositpaid'] != old_person['depositpaid'], 'Внесение совпадает'
        assert new_person['bookingdates']['checkin'] != old_person['bookingdates']['checkin'], 'Даты входа совпадают'
        assert new_person['bookingdates']['checkout'] != old_person['bookingdates']['checkout'], 'Даты выхода совпадают'
        assert new_person['additionalneeds'] != old_person['additionalneeds'], 'Запросы клиента совпадают'

        delete_booking = auth_session.delete(f"{BASE_URL}/booking/{booking_id}")
        assert delete_booking.status_code == 201, f"Ошибка при удалении букинга с ID {booking_id}"

        get_deleted_booking = auth_session.get(f"{BASE_URL}/booking/{booking_id}")
        assert get_deleted_booking.status_code == 404, "Букинг не был удален"

    def test_patch_booking(self, booking_data, auth_session): #как правильно сполиморфить?
        create_booking = auth_session.post(f"{BASE_URL}/booking", json=booking_data)
        booking_id = create_booking.json().get("bookingid")
        old_person = create_booking.json()['booking']
        update_booking = auth_session.patch(f"{BASE_URL}/booking/{booking_id}", json = {'firstname': 'IRINA'})
        assert update_booking.status_code == 200, 'Unavailable status code'
        new_person = update_booking.json()
        assert new_person['firstname'] != old_person['firstname'], 'Имена совпадают'
        assert new_person['lastname'] == old_person['lastname'], 'Фамилии не совпадают'
        assert new_person['totalprice'] == old_person['totalprice'], 'Суммы не совпадают'
        assert new_person['depositpaid'] == old_person['depositpaid'], 'Внесение не совпадает'

        delete_booking = auth_session.delete(f"{BASE_URL}/booking/{booking_id}")
        assert delete_booking.status_code == 201, f"Ошибка при удалении букинга с ID {booking_id}"

        get_deleted_booking = auth_session.get(f"{BASE_URL}/booking/{booking_id}")
        assert get_deleted_booking.status_code == 404, "Букинг не был удален"

    def test_get_booking(self, auth_session):
        get_booking_ids = auth_session.get(f'{BASE_URL}/booking')
        assert get_booking_ids.status_code == 200, 'неверный запрос'
        body_of_booking_ids = get_booking_ids.json()
        assert body_of_booking_ids is not None
        list_of_booking_ids = []
        for i in range(len(body_of_booking_ids)):
            ids = body_of_booking_ids[i]['bookingid']
            list_of_booking_ids.append(ids)

        def reducer(seen, element):
            if element in seen:
                raise ValueError("Обнаружен дубликат")
            seen.add(element)
            return seen

        try:
            reduce(reducer, set(), list_of_booking_ids)
        except ValueError:
            has_duplicates = True
        else:
            has_duplicates = False


class Test_negative_booking(TestBookings):

    def test_update_booking(self, booking_data, auth_session_with_basic, update_data):
        create_booking = auth_session_with_basic.post(f"{BASE_URL}/booking", json = booking_data)
        assert create_booking.status_code == 200, 'Unavailible status code'
        booking_id = create_booking.json().get("bookingid")
        auth_session_with_basic.headers.update({"Authorization": f"Something"})
        update_booking = auth_session_with_basic.put(f"{BASE_URL}/booking/{booking_id}", json = update_data)
        assert update_booking.status_code == 403, 'Нет ошибки Forbidden'
        auth_session_with_basic.headers.update({"Authorization": f"Basic YWRtaW46cGFzc3dvcmQxMjM="})
        delete_booking = auth_session_with_basic.delete(f"{BASE_URL}/booking/{booking_id}")
        assert delete_booking.status_code == 201, f"Ошибка при удалении букинга с ID {booking_id}"

        get_deleted_booking = auth_session_with_basic.get(f"{BASE_URL}/booking/{booking_id}")
        assert get_deleted_booking.status_code == 404, "Букинг не был удален"


    def test_update_zero(self,auth_session_with_basic,update_data,create_zero_id):
        get_booking = auth_session_with_basic.get(f"{BASE_URL}/booking/{create_zero_id}")
        assert get_booking.status_code == 404, 'Найден существующий id'
        update_booking = auth_session_with_basic.put(f"{BASE_URL}/booking/{create_zero_id}", json=update_data)
        assert update_booking.status_code == 405, 'Изменен несуществующий id'

    def test_unavailable_data(self,auth_session,booking_data,update_wrong_data):
        create_booking = auth_session.post(f"{BASE_URL}/booking", json=booking_data)
        assert create_booking.status_code == 200, 'Unavailible status code'
        booking_id = create_booking.json().get("bookingid")
        update_wrong_booking = auth_session.put(f"{BASE_URL}/booking/{booking_id}", json=update_wrong_data)
        try:
            assert update_wrong_booking.status_code == 400, ValueError(f'Принят неверный формат "depositpaid"')
            return ValueError
        finally:
            delete_booking = auth_session.delete(f"{BASE_URL}/booking/{booking_id}")
            assert delete_booking.status_code == 201, f"Ошибка при удалении букинга с ID {booking_id}"

            get_deleted_booking = auth_session.get(f"{BASE_URL}/booking/{booking_id}")
            assert get_deleted_booking.status_code == 404, "Букинг не был удален"


