import allure
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import BASE_URL_UI


@allure.feature("UI")
@allure.story("Поиск")
@allure.title("Поиск фильма по ключевому слову на кириллице")
@pytest.mark.ui
def test_search_cyrillic() -> None:
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 20)

    try:
        with allure.step("Открыть сайт Кинопоиска"):
            driver.get(BASE_URL_UI)

        with allure.step("Ввести 'Лев' в строку поиска"):
            search_input = wait.until(
                EC.presence_of_element_located(
                    (By.CSS_SELECTOR, "input[name='text']")
                )
            )
            search_input.send_keys("Лев")

        with allure.step("Нажать Enter"):
            search_input.submit()

        with allure.step("Дождаться результатов поиска"):
            results = wait.until(
                EC.presence_of_all_elements_located(
                    (By.CSS_SELECTOR, "a.base-movie-main-info_link__K161e")
                )
            )

        with allure.step("Проверить, что результаты найдены"):
            assert len(results) > 0
    finally:
        try:
            driver.quit()
        except Exception:
            pass
