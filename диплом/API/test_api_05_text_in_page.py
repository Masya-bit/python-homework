import allure
import pytest
import requests
from config import BASE_URL_API, API_KEY

HEADERS = {"X-API-KEY": API_KEY}


@allure.feature("API")
@allure.story("Поиск")
@allure.title("Передача текста в числовой параметр page")
@pytest.mark.api
def test_search_text_in_page_param() -> None:
    with allure.step("Отправить GET-запрос с параметром page=ААА"):
        response = requests.get(
            f"{BASE_URL_API}/movie/search",
            headers=HEADERS,
            params={"page": "ААА"}
        )

    with allure.step("Проверить, что статус-код не 200"):
        assert response.status_code != 200
