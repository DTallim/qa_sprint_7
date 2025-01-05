ORDER_BASE_DATA ={
    "firstName": "Naruto",
    "lastName": "Uchiha",
    "address": "Konoha, 142 apt.",
    "metroStation": 4,
    "phone": "+7 800 355 35 35",
    "rentTime": 5,
    "deliveryData": "2025-06-06",
    "comment":"Saske, come back to Konoha",
}

ORDER_DATA_VARIANTS = [
    {**ORDER_BASE_DATA, "color": ["BLACK"]},
    {**ORDER_BASE_DATA, "color":["GREY"]},
    {**ORDER_BASE_DATA, "color":["BLACK","GREY"]},
    ORDER_BASE_DATA.copy()
]

COURIER_EXIST_MESSAGE = 'Этот логин уже используется. Попробуйте другой'
CREATE_ACCOUNT_NOT_ENOUGH_DATA = 'Недостаточно данных для создания учетной записи'
LOGIN_NOT_ENOUGH_DATA_MESSAGE = 'Недостаточно данных для входа'
COURIER_NOT_FOUND_MESSAGE = 'Учетная запись не найдена'