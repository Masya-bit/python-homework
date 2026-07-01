import allure
import pytest
import requests
from config import BASE_URL_API, API_KEY

HEADERS = {"X-API-KEY": API_KEY}


@allure.feature("API")
@allure.story("Фильмы")
@allure.title("Получение списка фильмов")
@pytest.mark.api
def test_get_movies_list() -> None:
    with allure.step("Отправить GET-запрос на /movie"):
        response = requests.get(
            f"{BASE_URL_API}/movie",
            headers=HEADERS
        )

    with allure.step("Проверить, что статус-код 200"):
        assert response.status_code == 200

    with allure.step("Проверить, что ответ содержит массив docs"):
        body = response.json()
        assert "docs" in body
        assert len(body["docs"]) > 0
