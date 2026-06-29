import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SlowCalculatorPage:

    URL: str = (
        "https://bonigarcia.dev/selenium-webdriver-java/"
        "slow-calculator.html"
    )
    """Адрес страницы медленного калькулятора."""

    def __init__(self, driver: webdriver.Chrome) -> None:

        self.driver: webdriver.Chrome = driver

        self.wait: WebDriverWait = WebDriverWait(driver, 10)

        self._delay_field: tuple[str, str] = (By.CSS_SELECTOR, "#delay")

        self._screen: tuple[str, str] = (By.CSS_SELECTOR, ".screen")

        self._button_template: str = "//span[text()='{}']"

    @allure.step("Открыть страницу калькулятора")
    def open(self) -> None:

        self.driver.get(self.URL)

    @allure.step("Установить задержку {seconds} секунд")
    def set_delay(self, seconds: int) -> None:

        field = self.wait.until(
            EC.presence_of_element_located(self._delay_field)
        )
        field.clear()
        field.send_keys(str(seconds))

    @allure.step("Нажать кнопку '{label}'")
    def click_button(self, label: str) -> None:

        locator: tuple[str, str] = (
            By.XPATH,
            self._button_template.format(label)
        )
        button = self.wait.until(
            EC.element_to_be_clickable(locator)
        )
        button.click()

    @allure.step("Дождаться результата '{expected_text}'")
    def wait_for_result(self, expected_text: str, timeout: int = 60) -> str:

        WebDriverWait(self.driver, timeout).until(
            EC.text_to_be_present_in_element(self._screen, expected_text)
        )
        return self.driver.find_element(*self._screen).text


@allure.feature("Калькулятор")
@allure.title("Проверка вычисления 7 + 8 с задержкой 45 секунд")
@allure.description(
    "Тест проверяет, что медленный калькулятор корректно "
    "вычисляет сумму 7 + 8 и отображает результат '15' "
    "через заданную задержку в 45 секунд."
)
@allure.severity(allure.severity_level.CRITICAL)
def test_slow_calculator() -> None:

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


if __name__ == "__main__":
    test_slow_calculator()