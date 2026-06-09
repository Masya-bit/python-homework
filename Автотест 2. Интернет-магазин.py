from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    """Страница авторизации."""

    URL = "https://www.saucedemo.com/"

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self._username = (By.ID, "user-name")
        self._password = (By.ID, "password")
        self._login_button = (By.ID, "login-button")

    def open(self):
        self.driver.get(self.URL)

    def login(self, username: str, password: str):
        self.wait.until(
            EC.presence_of_element_located(self._username)
        ).send_keys(username)
        self.driver.find_element(*self._password).send_keys(password)
        self.driver.find_element(*self._login_button).click()


class InventoryPage:
    """Главная страница с товарами."""

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self._add_backpack = (By.ID, "add-to-cart-sauce-labs-backpack")
        self._add_bolt_tshirt = (
            By.ID, "add-to-cart-sauce-labs-bolt-t-shirt"
        )
        self._add_onesie = (By.ID, "add-to-cart-sauce-labs-onesie")
        self._cart_link = (By.CSS_SELECTOR, ".shopping_cart_link")

    def add_item(self, item_id: str):
        element = self.wait.until(
            EC.element_to_be_clickable((By.ID, item_id))
        )
        element.click()

    def add_backpack(self):
        self.add_item("add-to-cart-sauce-labs-backpack")

    def add_bolt_tshirt(self):
        self.add_item("add-to-cart-sauce-labs-bolt-t-shirt")

    def add_onesie(self):
        self.add_item("add-to-cart-sauce-labs-onesie")

    def go_to_cart(self):
        self.driver.find_element(*self._cart_link).click()


class CartPage:
    """Страница корзины."""

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self._checkout_button = (By.ID, "checkout")

    def checkout(self):
        self.wait.until(
            EC.element_to_be_clickable(self._checkout_button)
        ).click()


class CheckoutPage:
    """Страница оформления заказа."""

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self._first_name = (By.ID, "first-name")
        self._last_name = (By.ID, "last-name")
        self._postal_code = (By.ID, "postal-code")
        self._continue_button = (By.ID, "continue")
        self._total_label = (By.CSS_SELECTOR, ".summary_total_label")

    def fill_form(self, first_name: str, last_name: str, postal_code: str):
        self.wait.until(
            EC.presence_of_element_located(self._first_name)
        ).send_keys(first_name)
        self.driver.find_element(*self._last_name).send_keys(last_name)
        self.driver.find_element(*self._postal_code).send_keys(postal_code)

    def continue_to_overview(self):
        self.driver.find_element(*self._continue_button).click()

    def get_total(self) -> str:
        element = self.wait.until(
            EC.presence_of_element_located(self._total_label)
        )
        return element.text


def test_saucedemo_checkout():
    driver = webdriver.Firefox()

    try:
        login_page = LoginPage(driver)
        inventory_page = InventoryPage(driver)
        cart_page = CartPage(driver)
        checkout_page = CheckoutPage(driver)

        login_page.open()
        login_page.login("standard_user", "secret_sauce")

        inventory_page.add_backpack()
        inventory_page.add_bolt_tshirt()
        inventory_page.add_onesie()

        inventory_page.go_to_cart()

        cart_page.checkout()

        checkout_page.fill_form("Максим", "Тараканов", "669900")
        checkout_page.continue_to_overview()

        total = checkout_page.get_total()

        assert total == "Total: $58.29", (
            f"Ожидалась сумма Total: $58.29, но отобразилось {total}"
        )
    finally:
        driver.quit()


if __name__ == "__main__":
    test_saucedemo_checkout()