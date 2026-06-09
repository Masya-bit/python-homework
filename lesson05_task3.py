from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service
import time

service = Service(GeckoDriverManager().install())
driver = webdriver.Firefox(service=service)

try:
    driver.get("http://the-internet.herokuapp.com/inputs")

    input_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "input"))
    )

    input_field.send_keys("12345")
    time.sleep(5)

    input_field.clear()
    time.sleep(5)

    input_field.send_keys("54321")
    time.sleep(5)


finally:
    driver.quit()