import allure

from conftest import login_courier
from methods.courier_methods import CourierMethods
from methods.order_methods import OrderMethods

class TestGetOrdersList:
    @allure.title('Тест получения списка всех заказов без фильтра по курьеру')
    def test_get_all_orders(self):
        response = OrderMethods().get_orders()  # Remove the courier_id parameter completely
        assert response.status_code == 200
        assert "orders" in response.json()

    @allure.title('Тест получения списка заказов с пустым ID курьера')
    def test_get_orders_with_empty_courier(self):
        response = OrderMethods().get_orders(courier_id='')  # Use empty string instead of None
        assert response.status_code == 200
        assert "orders" in response.json()

    @allure.title('Тест получения списка заказов конкретного курьера')
    def test_get_courier_orders(self, login_courier):
        # Логинимся курьером для получения id
        login_response = CourierMethods().login_courier(login_courier[0])
        assert login_response.status_code == 200
        courier_id = login_response.json()['id']

        # Получаем заказы курьера
        response = OrderMethods().get_orders(courier_id=courier_id)
        assert response.status_code == 200
        assert "orders" in response.json()