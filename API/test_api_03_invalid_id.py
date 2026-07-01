import allure
import pytest
import requests
from config import BASE_URL_API, API_KEY

HEADERS = {"X-API-KEY": API_KEY}


@allure.feature("API")
@allure.story("Фильмы")
@allure.title("Запрос фильма с несуществующим ID")
@pytest.mark.api
def test_get_movie_invalid_id() -> None:
    with allure.step("Отправить GET-запрос на /movie/999999999"):
        response = requests.get(
            f"{BASE_URL_API}/movie/999999999",
            headers=HEADERS
        )

    with allure.step("Проверить, что статус-код не 200"):
        assert response.status_code != 200

    with allure.step("Проверить, что ответ содержит сообщение об ошибке"):
        body = response.json()
        assert "message" in body
