import allure
import requests
from config import BASE_URL, CREATE_COURIER, LOGIN_COURIER, DELETE_COURIER

class CourierMethods:
    @allure.step('Создание курьера')
    def create_courier(self, payload):
        url = f'{BASE_URL}{CREATE_COURIER}'
        response = requests.post(url, json=payload)
        allure.attach(f"URL: {url}\nPayload: {payload}\nStatus: {response.status_code}\nResponse: {response.text}",
                     'Request Details', allure.attachment_type.TEXT)
        return response

    @allure.step('Авторизация курьера')
    def login_courier(self, payload):
        url = f'{BASE_URL}{LOGIN_COURIER}'
        response = requests.post(url, json=payload)
        allure.attach(f"URL: {url}\nPayload: {payload}\nStatus: {response.status_code}\nResponse: {response.text}",
                     'Request Details', allure.attachment_type.TEXT)
        return response

    @allure.step('Удаление курьера')
    def delete_courier(self, courier_id):
        url = f'{BASE_URL}{DELETE_COURIER}/{courier_id}'
        response = requests.delete(url)
        allure.attach(f"URL: {url}\nStatus: {response.status_code}\nResponse: {response.text}",
                     'Request Details', allure.attachment_type.TEXT)
        return response