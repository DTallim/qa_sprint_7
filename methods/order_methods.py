import allure
import requests
from config import BASE_URL, CREATE_ORDER, ORDER_LIST


class OrderMethods:
    @allure.step('Вызов метода POST для создания заказа')
    def post_order(self, params):
        url = f'{BASE_URL}{CREATE_ORDER}'
        response = requests.post(url, json=params)
        allure.attach(f"URL: {url}\nPayload: {params}\nStatus: {response.status_code}\nResponse: {response.text}",
                      'Request Details', allure.attachment_type.TEXT)
        return response

    @allure.step('Вызов метода GET для получения списка заказов курьера')
    def get_orders(self, courier_id=None):
        url = f'{BASE_URL}/api/v1/orders'  # используем базовый URL для заказов
        params = {'courierId': courier_id} if courier_id else None

        response = requests.get(url, params=params)
        allure.attach(f"URL: {url}\nParams: {params}\nStatus: {response.status_code}\nResponse: {response.text}",
                      'Request Details', allure.attachment_type.TEXT)
        return response