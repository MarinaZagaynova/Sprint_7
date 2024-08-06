import allure
import pytest
import requests

from endpoints import Endpoints
import helps


class TestLogin:
    @allure.title('Проверка авторизации курьера')
    def test_login(self):
        response = requests.post(Endpoints.login_courier,
                                 data=helps.payload_correct_for_authorization)
        assert response.status_code == 200

    @allure.title('Проверка передачи всех обязательных полей. если одного из полей нет, запрос возвращает ошибку')
    # комментарий для ревьюера. Тест разделен на 2, т.к. в документации ошибка. Обсудили с наставником, проверяю по двум разным ответам
    @pytest.mark.parametrize('payload', [helps.payload_empty_for_authorization,
                                         helps.payload_without_password_for_authorization])
    def test_required_fields_for_login(self, payload):
        response = requests.post(Endpoints.login_courier, data=payload)
        assert response.text == 'Service unavailable'

    @allure.title('Проверка передачи всех обязательных полей. если одного из полей нет, запрос возвращает ошибку')
    def test_required_fields_for_without_login(self):
        response = requests.post(Endpoints.login_courier,
                                 data=helps.payload_without_login_for_authorization)
        assert response.text == '{"code":400,"message":"Недостаточно данных для входа"}'

    @allure.title('Проверка некорректного логина или пароля, пользователя не существует. запрос возвращает ошибку')
    def test_not_correct(self):
        payload = {
            "login": "не существует",
            "password": "не существует",
        }
        response = requests.post(Endpoints.login_courier, data=payload)
        assert response.status_code == 404 and response.text == '{"code":404,"message":"Учетная запись не найдена"}'

    @allure.title('Проверка: успешный запрос авторизации курьера возвращает id курьера')
    def test_login_text(self):
        response = requests.post(Endpoints.login_courier,
                                 data=helps.payload_correct_for_authorization)
        assert 'id' in response.text
