from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SlowCalculatorPage:
    """Page Object для страницы медленного калькулятора."""

    URL = (
        "https://bonigarcia.dev/selenium-webdriver-java/"
        "slow-calculator.html"
    )

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self._delay_field = (By.CSS_SELECTOR, "#delay")
        self._screen = (By.CSS_SELECTOR, ".screen")
        self._button_template = "//span[text()='{}']"

    def open(self):
        self.driver.get(self.URL)

    def set_delay(self, seconds: int):
        field = self.wait.until(
            EC.presence_of_element_located(self._delay_field)
        )
        field.clear()
        field.send_keys(str(seconds))

    def click_button(self, label: str):
        locator = (
            By.XPATH,
            self._button_template.format(label)
        )
        button = self.wait.until(
            EC.element_to_be_clickable(locator)
        )
        button.click()

    def wait_for_result(self, expected_text: str, timeout: int = 60) -> str:
        """Ожидает появления конкретного текста на экране."""
        WebDriverWait(self.driver, timeout).until(
            EC.text_to_be_present_in_element(self._screen, expected_text)
        )
        return self.driver.find_element(*self._screen).text


def test_slow_calculator():
    driver = webdriver.Chrome()
    calc = SlowCalculatorPage(driver)

    try:
        calc.open()
        calc.set_delay(45)

        buttons = ['7', '+', '8', '=']
        for btn in buttons:
            calc.click_button(btn)

        result = calc.wait_for_result("15", timeout=60)

        assert result == "15", (
            f"Ожидался результат '15', но отобразилось '{result}'"
        )
    finally:
        driver.quit()


if __name__ == "__main__":
    test_slow_calculator()