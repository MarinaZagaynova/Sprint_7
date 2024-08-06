import allure
import requests

from endpoints import Endpoints


class TestOrder:
    @allure.title('Проверка, что в тело ответа возвращается список заказов')
    def test_get_orders(self):
        response = requests.get(Endpoints.get_orders_list, params={'limit': 5})
        assert 'id' in response.text and response.status_code == 200
