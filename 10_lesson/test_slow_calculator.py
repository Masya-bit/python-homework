import allure
from selenium import webdriver
from slow_calculator_page import SlowCalculatorPage


@allure.feature("Калькулятор")
@allure.title("Проверка вычисления 7 + 8 с задержкой 45 секунд")
@allure.description(
    "Тест проверяет, что медленный калькулятор корректно "
    "вычисляет сумму 7 + 8 и отображает результат '15' "
    "через заданную задержку в 45 секунд."
)
@allure.severity(allure.severity_level.CRITICAL)
def test_slow_calculator() -> None:
    """
    Тест для проверки работы медленного калькулятора.

    :return: None
    """
    driver: webdriver.Chrome = webdriver.Chrome()
    calc: SlowCalculatorPage = SlowCalculatorPage(driver)

    try:
        with allure.step("Открыть страницу и настроить задержку"):
            calc.open()
            calc.set_delay(45)

        with allure.step("Выполнить вычисление: 7 + 8 ="):
            buttons: list[str] = ['7', '+', '8', '=']
            for btn in buttons:
                calc.click_button(btn)

        with allure.step("Получить результат вычисления"):
            result: str = calc.wait_for_result("15", timeout=60)

        with allure.step("Проверить, что результат равен '15'"):
            assert result == "15", (
                f"Ожидался результат '15', но отобразилось '{result}'"
            )
    finally:
        driver.quit()
