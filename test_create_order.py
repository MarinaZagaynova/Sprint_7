import json

import allure
import pytest
import requests

from endpoints import Endpoints
import helps


class TestCreateOrder:
    @allure.title('Проверка указания обоих цветов, только одного цвета в запросе создания заказа')
    @allure.description(
        'Отправляем запрос на создание заказа с поочередным добавлением различных цветов')
    @pytest.mark.parametrize('color', [helps.color_black_and_grey, helps.color_gray, helps.color_black])
    def test_color(self, color):
        payload = {
            "firstName": "Имя",
            "lastName": "Фамилия",
            "address": "Москва",
            "metroStation": 2,
            "phone": "89879879898",
            "rentTime": 2,
            "deliveryDate": "2024-06-25",
            "comment": "comment",
            "color": color
        }
        response = requests.post(Endpoints.create_order,
                                 data=json.dumps(payload))
        assert 'track' in response.text

    @allure.title('Проверка запроса созданния заказа без указания цвета. успешный запрос возвращает track')
    def test_without_color(self):
        response = requests.post(Endpoints.create_order,
                                 data=helps.payload_without_color)
        assert 'track' in response.text
