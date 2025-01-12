import allure
import pytest

from helpers import generate_login_password_name
from methods.courier_methods import CourierMethods


class TestCreateCourier:
    @allure.title('Тест регистрации курьера ("ok":true, статус ответа 201)')
    def test_create_courier(self):
        payload = generate_login_password_name()
        response = CourierMethods().create_courier(payload)

        # Удаляем созданного курьера
        login_data = {'login': payload['login'], 'password': payload['password']}
        login_response = CourierMethods().login_courier(login_data)
        if login_response.status_code == 200:
            CourierMethods().delete_courier(login_response.json()['id'])

        assert response.status_code == 201
        assert response.json() == {"ok": True}

    @allure.title('Тест невозможности регистрации двух одинаковых курьеров (статус ответа 409)')
    def test_create_two_identical_couriers(self):
        payload = generate_login_password_name()
        # Создаем первого курьера
        CourierMethods().create_courier(payload)
        # Пытаемся создать второго курьера с теми же данными
        response = CourierMethods().create_courier(payload)

        # Удаляем тестового курьера
        login_data = {'login': payload['login'], 'password': payload['password']}
        login_response = CourierMethods().login_courier(login_data)
        if login_response.status_code == 200:
            CourierMethods().delete_courier(login_response.json()['id'])

        assert response.status_code == 409
        assert response.json()['message'] == 'Этот логин уже используется. Попробуйте другой.'

    @allure.title('Тест невозможности регистрации курьера без обязательных полей')
    @pytest.mark.parametrize('empty_field_name', ["login", "password"])
    def test_create_courier_with_empty_field_login_or_password(self, empty_field_name):
        payload = generate_login_password_name()
        payload[empty_field_name] = ''
        response = CourierMethods().create_courier(payload)
        assert response.status_code == 400
        assert response.json()['message'] == 'Недостаточно данных для создания учетной записи'

    @allure.title('Тест регистрации курьера без имени')
    def test_create_courier_with_empty_field_first_name(self):
        payload = generate_login_password_name()
        payload['firstName'] = ''
        response = CourierMethods().create_courier(payload)

        # Удаляем тестового курьера
        if response.status_code == 201:
            login_data = {'login': payload['login'], 'password': payload['password']}
            login_response = CourierMethods().login_courier(login_data)
            if login_response.status_code == 200:
                CourierMethods().delete_courier(login_response.json()['id'])

        assert response.status_code == 201
        assert response.json() == {"ok": True}