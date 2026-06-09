from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.edge.service import Service


def test_data_types():
    driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))

    try:
        # 1. Открываем страницу
        driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

        # 2. Заполняем форму
        wait = WebDriverWait(driver, 10)

        field = wait.until(EC.presence_of_element_located((By.NAME, "first-name")))
        field.send_keys("Иван")

        field = driver.find_element(By.NAME, "last-name")
        field.send_keys("Петров")

        field = driver.find_element(By.NAME, "address")
        field.send_keys("Ленина, 55-3")

        field = driver.find_element(By.NAME, "e-mail")
        field.send_keys("test@skypro.com")

        field = driver.find_element(By.NAME, "phone")
        field.send_keys("+7985899998787")

        field = driver.find_element(By.NAME, "city")
        field.send_keys("Москва")

        field = driver.find_element(By.NAME, "country")
        field.send_keys("Россия")

        field = driver.find_element(By.NAME, "job-position")
        field.send_keys("QA")

        field = driver.find_element(By.NAME, "company")
        field.send_keys("SkyPro")

        # 3. Нажимаем Submit
        submit_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
        submit_button.click()

        # 4. Проверяем, что Zip code подсвечен красным
        zip_code_field = wait.until(
            EC.presence_of_element_located((By.ID, "zip-code"))
        )
        assert "alert-danger" in zip_code_field.get_attribute("class") or \
               "is-invalid" in zip_code_field.get_attribute("class") or \
               "invalid" in zip_code_field.get_attribute("class"), \
               "Zip code должен быть подсвечен красным"

        # 5. Проверяем, что остальные поля подсвечены зелёным
        green_field_ids = [
            "first-name",
            "last-name",
            "address",
            "e-mail",
            "phone",
            "city",
            "country",
            "job-position",
            "company"
        ]

        for field_id in green_field_ids:
            field = driver.find_element(By.ID, field_id)
            assert "alert-success" in field.get_attribute("class") or \
                   "is-valid" in field.get_attribute("class") or \
                   "valid" in field.get_attribute("class"), \
                   f"Поле {field_id} должно быть подсвечено зелёным"

    finally:
        driver.quit()


if __name__ == "__main__":
    test_data_types()