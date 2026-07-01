import allure
import pytest
import requests
from config import BASE_URL_API


@allure.feature("API")
@allure.story("Авторизация")
@allure.title("Запрос к API без ключа")
@pytest.mark.api
def test_request_without_api_key() -> None:
    with allure.step("Отправить GET-запрос без заголовка X-API-KEY"):
        response = requests.get(
            f"{BASE_URL_API}/movie/11650886"
        )

    with allure.step("Проверить, что статус-код 401"):
        assert response.status_code == 401
