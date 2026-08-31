from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SlowCalculatorPage:
    """
    Page Object для страницы медленного калькулятора.

    Инкапсулирует взаимодействие с элементами страницы:
    поле задержки, кнопки цифр и операций, экран результата.
    """

    URL: str = (
        "https://bonigarcia.dev/selenium-webdriver-java/"
        "slow-calculator.html"
    )
    """Адрес страницы медленного калькулятора."""

    def __init__(self, driver: webdriver.Chrome) -> None:
        """
        Инициализация страницы калькулятора.

        :param driver: экземпляр веб-драйвера Chrome.
        :type driver: webdriver.Chrome
        :return: None
        """
        self.driver: webdriver.Chrome = driver
        """Экземпляр веб-драйвера Chrome."""

        self.wait: WebDriverWait = WebDriverWait(driver, 10)
        """Явное ожидание с таймаутом 10 секунд."""

        self._delay_field: tuple[str, str] = (By.CSS_SELECTOR, "#delay")
        """Локатор поля ввода задержки."""

        self._screen: tuple[str, str] = (By.CSS_SELECTOR, ".screen")
        """Локатор экрана с результатом вычислений."""

        self._button_template: str = "//span[text()='{}']"
        """Шаблон XPath-локатора для кнопок калькулятора."""

    def open(self) -> None:
        """
        Открывает страницу медленного калькулятора в браузере.

        :return: None
        """
        self.driver.get(self.URL)

    def set_delay(self, seconds: int) -> None:
        """
        Вводит значение задержки в поле #delay.

        :param seconds: количество секунд задержки перед
            отображением результата.
        :type seconds: int
        :return: None
        """
        field = self.wait.until(
            EC.presence_of_element_located(self._delay_field)
        )
        field.clear()
        field.send_keys(str(seconds))

    def click_button(self, label: str) -> None:
        """
        Нажимает кнопку калькулятора по её тексту.

        :param label: текст на кнопке (например, '7', '+', '=').
        :type label: str
        :return: None
        """
        locator: tuple[str, str] = (
            By.XPATH,
            self._button_template.format(label)
        )
        button = self.wait.until(
            EC.element_to_be_clickable(locator)
        )
        button.click()

    def wait_for_result(self, expected_text: str, timeout: int = 60) -> str:
        """
        Ожидает появления заданного текста на экране калькулятора
        и возвращает его.

        :param expected_text: ожидаемый текст результата
            (например, '15').
        :type expected_text: str
        :param timeout: максимальное время ожидания в секундах.
        :type timeout: int
        :return: текст, отображаемый на экране калькулятора.
        :rtype: str
        """
        WebDriverWait(self.driver, timeout).until(
            EC.text_to_be_present_in_element(self._screen, expected_text)
        )
        return self.driver.find_element(*self._screen).text


def test_slow_calculator() -> None:
    """
    Тест для проверки работы медленного калькулятора.

    Открывает страницу, вводит задержку 45 секунд,
    выполняет операцию 7 + 8 = и проверяет,
    что результат равен '15'.

    :return: None
    """
    driver: webdriver.Chrome = webdriver.Chrome()
    calc: SlowCalculatorPage = SlowCalculatorPage(driver)

    try:
        calc.open()
        calc.set_delay(45)

        buttons: list[str] = ['7', '+', '8', '=']
        for btn in buttons:
            calc.click_button(btn)

        result: str = calc.wait_for_result("15", timeout=60)

        assert result == "15", (
            f"Ожидался результат '15', но отобразилось '{result}'"
        )
    finally:
        driver.quit()


if __name__ == "__main__":
    test_slow_calculator()
