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
    
    driver.get("http://the-internet.herokuapp.com/login")

    username_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "username"))
    )
    username_field.send_keys("tomsmith")

    password_field = driver.find_element(By.ID, "password")
    password_field.send_keys("SuperSecretPassword!")

    login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
    login_button.click()

    success_message = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".flash.success"))
    )
    print(success_message.text)

finally:
    time.sleep(2) 
    driver.quit()