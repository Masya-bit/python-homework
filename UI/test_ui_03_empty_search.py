import allure
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import BASE_URL_UI


@allure.feature("UI")
@allure.story("Поиск")
@allure.title("Проверка обработки пустого поискового запроса")
@pytest.mark.ui
def test_search_empty() -> None:
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)

    try:
        with allure.step("Открыть сайт Кинопоиска"):
            driver.get(BASE_URL_UI)

        with allure.step("Найти поле поиска и очистить его"):
            search_input = wait.until(
                EC.presence_of_element_located(
                    (By.CSS_SELECTOR, "input[name='text']")
                )
            )
            search_input.clear()

        with allure.step("Проверить, что поле пустое"):
            assert search_input.get_attribute("value") == ""
    finally:
        try:
            driver.quit()
        except Exception:
            pass
