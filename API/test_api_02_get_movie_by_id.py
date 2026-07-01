import allure
import pytest
import requests
from config import BASE_URL_API, API_KEY

HEADERS = {"X-API-KEY": API_KEY}


@allure.feature("API")
@allure.story("Фильмы")
@allure.title("Получение фильма по ID")
@pytest.mark.api
def test_get_movie_by_id() -> None:
    with allure.step("Отправить GET-запрос на /movie/11650886"):
        response = requests.get(
            f"{BASE_URL_API}/movie/11650886",
            headers=HEADERS
        )

    with allure.step("Проверить, что статус-код 200"):
        assert response.status_code == 200

    with allure.step("Проверить, что ответ содержит поле name или title"):
        body = response.json()
        assert "name" in body or "title" in body
