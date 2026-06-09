from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import time


def test_dynamic_loading():
    driver = webdriver.Chrome()

    try:
        # 1. Откройте страницу
        driver.get("https://the-internet.herokuapp.com/dynamic_loading/2")


        # 2. Найдите и нажмите на кнопку "Start"
        start_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#start button"))
        )
        start_button.click()

        # 3. Дождитесь появления текста "Hello World!"
        hello_text = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#finish h4"))
        )

        # 4. Сделайте скриншот страницы
        time.sleep(1)

        # Путь к рабочему столу
        desktop = os.path.join(os.path.expanduser("~"), "Desktop")
        screenshot_path = os.path.join(desktop, "screenshot.png")

        # Сохраняем скриншот
        result = driver.save_screenshot(screenshot_path)

        # Проверяем, сохранился ли файл
        if os.path.exists(screenshot_path):
            file_size = os.path.getsize(screenshot_path)
        else:
            driver.save_screenshot("screenshot.png")
            print(f"✓ Сохранён в текущую папку: {os.path.abspath('screenshot.png')}")

        # 5. Проверьте, что появившийся текст равен "Hello World!"
        actual_text = hello_text.text
        assert actual_text == "Hello World!", f"Ошибка! Ожидалось 'Hello World!', а получено '{actual_text}'"
        print(f"Проверка пройдена. Текст: '{actual_text}'")

    except AssertionError as e:
        print(f"✗ ПРОВАЛ ПРОВЕРКИ: {e}")
        driver.save_screenshot(os.path.join(desktop, "error_screenshot.png"))
        print("✓ Скриншот ошибки сохранён")
        raise

    except Exception as e:
        print(f"✗ ОШИБКА: {e}")
        raise

    finally:
        time.sleep(1)
        driver.quit()


if __name__ == "__main__":
    test_dynamic_loading()