import allure
import requests

import helps
from endpoints import Endpoints

import pytest

from helps import register_new_courier_and_return_login_password


class TestsCourier:
    @allure.title('Проверка создания курьера')
    def test_create_courier(self):
        logins = register_new_courier_and_return_login_password()
        assert logins != []

    @allure.title('Проверка создания пользователя с логином, который уже есть. Возвращается ошибка')
    def test_create_courier_two_identical_login_show_error(self):
        logins = register_new_courier_and_return_login_password()
        payload = {
            "login": logins[0],
            "password": logins[1],
            "firstName": logins[2]
        }
        requests.post(Endpoints.create_courier, data=payload)
        response = requests.post(Endpoints.create_courier, data=payload)
        assert response.status_code == 409 and response.text == '{"code":409,"message":"Этот логин уже используется. Попробуйте другой."}'

    @allure.title('Проверка создания двух одинаковых курьеров. Возвращается ошибка')
    def test_create_courier_two_identical_show_error(self):
        payload = {
            "login": 'identical',
            "password": 'identical',
            "firstName": 'identical'
        }
        requests.post(Endpoints.create_courier, data=payload)
        response = requests.post(Endpoints.create_courier, data=payload)
        assert response.status_code == 409 and response.text == '{"code":409,"message":"Этот логин уже используется. Попробуйте другой."}'

    @allure.title('Проверка передачи всех обязательных полей. если одного из полей нет, запрос возвращает ошибку')
    @pytest.mark.parametrize('payload', [helps.payload_without_login_for_registration,
                                         helps.payload_without_password_for_registration,
                                         helps.payload_empty_for_registration])
    def test_required_fields(self, payload):
        response = requests.post(Endpoints.create_courier, data=payload)
        assert response.text == '{"code":400,"message":"Недостаточно данных для создания учетной записи"}'

    @allure.title(
        'Проверка эндпоинта регистрации курьера с корректными входнымипараметрами. В ответе код 201 и текст = "ok":true')
    def test_correct_code(self):
        response = requests.post(Endpoints.create_courier,
                                 data=helps.payload_correct_for_registration)
        assert response.status_code == 201 and response.text == '{"ok":true}'
