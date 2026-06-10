from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def test_session_storage_auth():
    driver = webdriver.Chrome()

    # Куки пользователя 1
    user1_cookies = {
        "SESSION": "Y2M0ODkxOTEtMzYxNC00ZTRhLTljOWUtYmFjYWRmODgzZmRk",
        "Session_id": "3:1778450541.5.0.1765377264040:vTGTLg:5c46.1.2:1|766472777.-1.2.3:1765377264|3:11895644.924181.FRBpoITclPNc0QdPgZh_F2ohFdg",
        "X-CSRF-TOKEN": "d5fc2e8d-d188-468a-8582-479216463758",
        "sessionid2": "3:1778450541.5.0.1765377264040:vTGTLg:5c46.1.2:1|766472777.-1.2.3:1765377264|3:11895644.924181.fakesign0000000000000000000"
    }

    # Куки пользователя 2
    user2_cookies = {
        "SESSION": "MGZlMDU4NTYtYjc2YS00YWU2LWIwNGUtMGEyNzc3Nzc3YmQy",
        "Session_id": "3:1778450541.5.0.1765377264040:vTGTLg:5c46.1.2:1|766472777.-1.2.3:1765377264|3:11895644.924181.FRBpoITclPNc0QdPgZh_F2ohFdg",
        "X-CSRF-TOKEN": "7906950d-2b7e-4ecb-b93e-845ee9b162f6",
        "sessionid2": "3:1778450541.5.0.1765377264040:vTGTLg:5c46.1.2:1|766472777.-1.2.3:1765377264|3:11895644.924181.fakesign0000000000000000000"
    }

    try:
        # =================== ПОЛЬЗОВАТЕЛЬ 1 ===================
        print("\n=== ПОЛЬЗОВАТЕЛЬ 1 ===")

        driver.get("https://gitflic.ru/")

        for name, value in user1_cookies.items():
            driver.add_cookie({"name": name, "value": value, "domain": ".gitflic.ru"})

        driver.refresh()
        time.sleep(3)

        # Пробуем найти ссылку на профиль в разных местах
        try:
            # Ищем любую ссылку, которая может вести на профиль
            profile_element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "[class*='user'], [class*='profile'], [class*='account'], [href*='project'], [class*='avatar']"))
            )
            # Если нашли аватар или имя пользователя - кликаем
            clickable = driver.find_element(By.CSS_SELECTOR, "a[class*='user'], a[class*='profile'], a[class*='account'], a[class*='avatar'], [class*='avatar'] a, [class*='user'] a")
            clickable.click()
            time.sleep(2)
        except:
            # Если не нашли - пробуем перейти по ссылке вида /project/ или /user/
            try:
                user_links = driver.find_elements(By.CSS_SELECTOR, "a[href*='/project/']")
                if user_links:
                    user_links[0].click()
                    time.sleep(2)
            except:
                print("Не удалось найти ссылку на профиль, пробуем альтернативный метод")
                # Пробуем найти выпадающее меню пользователя
                try:
                    menu_triggers = driver.find_elements(By.CSS_SELECTOR, "[class*='dropdown'], [class*='menu'], [aria-haspopup]")
                    for trigger in menu_triggers:
                        if trigger.is_displayed():
                            trigger.click()
                            time.sleep(1)
                            break
                except:
                    pass

        url_user1 = driver.current_url
        print(f"URL пользователя 1: {url_user1}")

        # =================== РАЗЛОГИН ===================
        print("\n=== РАЗЛОГИН ===")

        driver.delete_all_cookies()

        # =================== ПОЛЬЗОВАТЕЛЬ 2 ===================
        print("\n=== ПОЛЬЗОВАТЕЛЬ 2 ===")

        driver.get("https://gitflic.ru/")

        for name, value in user2_cookies.items():
            driver.add_cookie({"name": name, "value": value, "domain": ".gitflic.ru"})

        driver.refresh()
        time.sleep(3)

        # Такой же поиск профиля для пользователя 2
        try:
            profile_element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "[class*='user'], [class*='profile'], [class*='account'], [href*='project'], [class*='avatar']"))
            )
            clickable = driver.find_element(By.CSS_SELECTOR, "a[class*='user'], a[class*='profile'], a[class*='account'], a[class*='avatar'], [class*='avatar'] a, [class*='user'] a")
            clickable.click()
            time.sleep(2)
        except:
            try:
                user_links = driver.find_elements(By.CSS_SELECTOR, "a[href*='/project/']")
                if user_links:
                    user_links[0].click()
                    time.sleep(2)
            except:
                print("Не удалось найти ссылку на профиль")

        url_user2 = driver.current_url
        print(f"URL пользователя 2: {url_user2}")

        # =================== ПРОВЕРКА ===================
        print("\n=== Проверка ===")

        assert url_user1 != url_user2, (
            f"Ошибка. URL совпадают!\n"
            f"   URL 1: {url_user1}\n"
            f"   URL 2: {url_user2}"
        )
        print("Проверка пройдена. URL различаются — пользователи разные.")

    except AssertionError as e:
        print(e)
        raise

    except Exception as e:
        print(f"Ошибка: {e}")
        raise

    finally:
        time.sleep(2)
        driver.quit()


if __name__ == "__main__":
    test_session_storage_auth()
