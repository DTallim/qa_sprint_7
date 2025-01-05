import allure
import pytest

from data import COURIER_EXIST_MESSAGE, CREATE_ACCOUNT_NOT_ENOUGH_DATA
from helpers import generate_login_password_name
from methods.courier_methods import CourierMethods


class TestCreateCourier:
    @allure.title("Успешное создание курьера")
    def test_create_courier(self):
        response = CourierMethods().create_courier(generate_login_password_name())
        assert response.status_code == 201
        assert response.json() == {"ok": True}

    @allure.title("Нельзя создать курьера с одинаковыми данными")
    def test_create_duplicate_courier(self):
        payload = generate_login_password_name()
        CourierMethods().create_courier(payload)
        response = CourierMethods().create_courier(payload)
        assert response.status_code == 409
        assert response.json().get("message") == COURIER_EXIST_MESSAGE

    @pytest.mark.parametrize(
        "payload", [
            {"password": "password_value", "firstName": "first_name_value"},
            {"login": "login_value", "firstName": "first_name_value"}
        ]
    )
    @allure.title("Отсутствует обязательное поле")
    def test_create_courier_with_error(self, payload):
        response = CourierMethods().create_courier(payload)
        assert response.status_code == 400
        assert response.json().get("message") == CREATE_ACCOUNT_NOT_ENOUGH_DATA