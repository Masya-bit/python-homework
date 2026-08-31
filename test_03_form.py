from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_saucedemo_checkout():
    driver = webdriver.Firefox()

    try:
        wait = WebDriverWait(driver, 10)

        # 1. Открываем сайт
        driver.get("https://www.saucedemo.com/")


        username = wait.until(EC.presence_of_element_located((By.ID, "user-name")))
        username.send_keys("standard_user")

        password = driver.find_element(By.ID, "password")
        password.send_keys("secret_sauce")

        login_button = driver.find_element(By.ID, "login-button")
        login_button.click()


        add_backpack = wait.until(
            EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-backpack"))
        )
        add_backpack.click()

        add_bolt_tshirt = driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
        add_bolt_tshirt.click()

        add_onesie = driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie")
        add_onesie.click()

        cart = driver.find_element(By.CSS_SELECTOR, ".shopping_cart_link")
        cart.click()

        checkout_button = wait.until(
            EC.element_to_be_clickable((By.ID, "checkout"))
        )
        checkout_button.click()

        first_name = wait.until(
            EC.presence_of_element_located((By.ID, "first-name"))
        )
        first_name.send_keys("Максим")

        last_name = driver.find_element(By.ID, "last-name")
        last_name.send_keys("Тараканов")

        postal_code = driver.find_element(By.ID, "postal-code")
        postal_code.send_keys("669900")

        continue_button = driver.find_element(By.ID, "continue")
        continue_button.click()

        total_element = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".summary_total_label"))
        )
        total_text = total_element.text

        driver.quit()

        assert total_text == "Total: $58.29", \
            f"Ожидалась сумма Total: $58.29, но отобразилось {total_text}"

    except Exception as e:
        driver.quit()
        raise e


if __name__ == "__main__":
    test_saucedemo_checkout()