import allure

from methods.order_methods import OrderMethods

class TestGetOrder:

    @allure.title("Полуение списка заказов")
    def test_get_order(self):
        response = OrderMethods().get_orders(742321)
        assert response.status_code == 200
        assert "orders" in response.json()