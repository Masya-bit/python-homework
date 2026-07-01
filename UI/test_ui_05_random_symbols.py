import allure
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import BASE_URL_UI


@allure.feature("UI")
@allure.story("Поиск")
@allure.title("Поиск по несвязанным между собой символам")
@pytest.mark.ui
def test_search_random_symbols() -> None:
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)

    try:
        with allure.step("Открыть сайт Кинопоиска"):
            driver.get(BASE_URL_UI)

        with allure.step("Ввести 'вапвап' в строку поиска"):
            search_input = wait.until(
                EC.presence_of_element_located(
                    (By.CSS_SELECTOR, "input[name='text']")
                )
            )
            search_input.send_keys("вапвап")

        with allure.step("Нажать Enter"):
            search_input.submit()

        with allure.step("Дождаться загрузки страницы"):
            wait.until(
                EC.presence_of_element_located((By.TAG_NAME, "body"))
            )

        with allure.step("Проверить, что URL содержит 'search'"):
            assert "search" in driver.current_url
    finally:
        try:
            driver.quit()
        except Exception:
            pass
