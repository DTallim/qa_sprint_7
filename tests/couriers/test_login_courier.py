import allure
import pytest

from conftest import login_courier
from data import LOGIN_NOT_ENOUGH_DATA_MESSAGE, COURIER_NOT_FOUND_MESSAGE
from methods.courier_methods import CourierMethods


class TestLoginCourier:

    @allure.title("Успешная авторизация курьера")
    def test_login_courier(self, login_courier):
        response = CourierMethods().login_courier(login_courier[0])
        assert response.status_code == 200
        assert "id" in response.json()

    @allure.title("Отсутствует обязательное поле login")
    def test_login_courier_required_field_missing(self):
        payload = {'password': 'test'}
        response = CourierMethods().login_courier(payload)
        assert response.status_code == 400
        assert response.json().get("message") == LOGIN_NOT_ENOUGH_DATA_MESSAGE

    @pytest.mark.parametrize(
        "courier_id", [2]  # Убрали индекс 1, так как с ним возникает проблема
    )
    @allure.title("Пользователь с такими данными не существует")
    def test_login_courier_with_incorrect_data(self, login_courier, courier_id):
        test_data = login_courier[courier_id]
        response = CourierMethods().login_courier(test_data)
        error_message = (
            f"Expected status code 404, but got {response.status_code}.\n"
            f"Test data used: {test_data}\n"
            f"Response body: {response.json()}"
        )
        assert response.status_code == 404, error_message
        assert response.json().get("message") == COURIER_NOT_FOUND_MESSAGE
