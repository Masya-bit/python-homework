import allure
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import BASE_URL_UI


@allure.feature("UI")
@allure.story("Карточка фильма")
@allure.title("Поиск по двум словам и проверка карточки фильма")
@pytest.mark.ui
def test_search_and_open_card() -> None:
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)

    try:
        with allure.step("Открыть сайт Кинопоиска"):
            driver.get(BASE_URL_UI)

        with allure.step("Ввести 'Король лев' в строку поиска"):
            search_input = wait.until(
                EC.presence_of_element_located(
                    (By.CSS_SELECTOR, "input[name='text']")
                )
            )
            search_input.send_keys("Король лев")

        with allure.step("Нажать Enter"):
            search_input.submit()

        with allure.step("Кликнуть на первый результат"):
            first_result = wait.until(
                EC.element_to_be_clickable(
                    (By.CSS_SELECTOR, "a.base-movie-main-info_link__K161e")
                )
            )
            first_result.click()

        with allure.step("Дождаться загрузки заголовка"):
            film_title = wait.until(
                EC.presence_of_element_located((By.TAG_NAME, "h1"))
            )

        with allure.step("Проверить, что заголовок содержит 'Король'"):
            assert "Король" in film_title.text
    finally:
        try:
            driver.quit()
        except Exception:
            pass
