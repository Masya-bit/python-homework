from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_slow_calculator():
    driver = webdriver.Chrome()

    try:
        
        driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

        wait = WebDriverWait(driver, 60)

        delay_field = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#delay")))
        delay_field.clear()
        delay_field.send_keys("45")

        btn_7 = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='7']")))
        btn_7.click()

        btn_plus = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='+']")))
        btn_plus.click()

        btn_8 = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='8']")))
        btn_8.click()

        btn_eq = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='=']")))
        btn_eq.click()

        wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".screen"), "15"))

        screen = driver.find_element(By.CSS_SELECTOR, ".screen")
        assert screen.text == "15", f"Ожидался результат 15, но отобразилось {screen.text}"

    finally:
        driver.quit()


if __name__ == "__main__":
    test_slow_calculator()