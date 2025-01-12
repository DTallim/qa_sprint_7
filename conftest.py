import pytest

from helpers import generate_login_password_name
from methods.courier_methods import CourierMethods


@pytest.fixture()
def login_courier():
    payload = generate_login_password_name()
    login_courier_body = {'login':payload.get('login'),'password': payload.get('password')}
    courier_incorrect_password = {'login': payload.get('login'), 'password': payload.get('password')}
    courier_incorrect_login = {'login':'qwerty','password': payload.get('password')}
    CourierMethods().create_courier(payload)
    yield login_courier_body, courier_incorrect_password,courier_incorrect_login
    response = CourierMethods().login_courier(login_courier_body)
    CourierMethods().delete_courier(response.json()['id'])