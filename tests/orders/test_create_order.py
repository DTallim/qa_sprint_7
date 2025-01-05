import allure
import pytest

from data import ORDER_DATA_VARIANTS
from methods.order_methods import (OrderMethods)

class TestCreateOrder:
    @pytest.mark.parametrize("payload",ORDER_DATA_VARIANTS)
    @allure.title("Создание заказа")
    def test_create_order(self,payload):
        response = OrderMethods().post_order(payload)
        assert response.status_code == 201
        assert "track" in  response.json()
