# ИМПОРТЫ
import random
import time
import config
from class_MySelenium import MySelenium
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait

# XPATH элементов
xpath_login = "//input[@name='username']"
xpath_password = "//input[@name='password']"
xpath_button = "//button[@type='submit']"
login = config.Login_insta
xpath_button_profile = f"//a[@role='link' and contains(@href, '/{login}/')]"
xpath_button_followers = "//a[@role='link' and contains(@href, '/followers/')]"
xpath_scroll_contain = '//div[@role="dialog"]//div[@class="xyi19xy x1ccrb07 xtf3nb5 x1pc53ja x1lliihq x1iyjqo2 xs83m0k xz65tgg x1rife3k x1n2onr6"]'


# Инициализация
obj = MySelenium()
obj.create_browser(headless=False)
wait = WebDriverWait(obj.BROWSER, 10)  # Инициализация ожидания

# Основной цикл для загрузки страницы
max_attempts = 10
attempt = 0

while attempt < max_attempts:
    try:
        obj.BROWSER.get("https://www.instagram.com/")
        wait.until(ec.presence_of_element_located((By.XPATH, xpath_login)))

        if obj.BROWSER.find_element(By.XPATH, xpath_login):
            break
        else:
            print(f"Попытка {attempt + 1} из {max_attempts}")
            obj.BROWSER.refresh()
            time.sleep(random.uniform(1, 2.5))
    except TimeoutException:
        print(f"Таймаут при загрузке страницы. Попытка {attempt + 1} из {max_attempts}")
        obj.BROWSER.refresh()
    except Exception as e:
        print(f"Произошла ошибка: {e}. Попытка {attempt + 1} из {max_attempts}")
        obj.BROWSER.refresh()
    finally:
        attempt += 1

if attempt == max_attempts:
    print("Не удалось выполнить загрузки страницы после нескольких попыток.")
else:
    print("Страница загружена, выполняем вход в аккаунт.")

# Дальнейший код (если условие выполнено)
try:
    # Ввод логина
    wait.until(ec.presence_of_element_located((By.XPATH, xpath_login)))
    elm_login = obj.BROWSER.find_element(By.XPATH, xpath_login)
    elm_login.send_keys(login)

    # Ввод пароля
    wait.until(ec.presence_of_element_located((By.XPATH, xpath_password)))
    time.sleep(random.uniform(1.5, 3.5))
    elm_password = obj.BROWSER.find_element(By.XPATH, xpath_password)
    elm_password.send_keys(config.Password_insta)

    # Нажатие на кнопку входа
    elm_button = obj.BROWSER.find_element(By.XPATH, xpath_button)
    elm_button.click()

    print(f"User name: {login}")  # Условие домашней работы

    # Переход в профиль
    wait.until(ec.presence_of_element_located((By.XPATH, xpath_button_profile)))
    time.sleep(random.uniform(1.5, 3.5))
    elm_button_profile = obj.BROWSER.find_element(By.XPATH, xpath_button_profile)
    elm_button_profile.click()

    # Открытие списка подписчиков
    wait.until(ec.presence_of_element_located((By.XPATH, xpath_button_followers)))
    time.sleep(random.uniform(1.5, 3.5))
    elm_button_followers = obj.BROWSER.find_element(By.XPATH, xpath_button_followers)
    elm_button_followers.click()
    print("Followers найдены")

    # Прокрутка списка подписчиков
    wait.until(ec.presence_of_element_located((By.XPATH, xpath_scroll_contain)))
    elm_scroll = obj.BROWSER.find_element(By.XPATH, xpath_scroll_contain)
    last_height = obj.BROWSER.execute_script("return arguments[0].scrollHeight", elm_scroll)

    scroll_attempts = 0
    max_scroll_attempts = 50  # максимальное количества попыток прокрутки можно изменять

    while scroll_attempts < max_scroll_attempts:
        obj.BROWSER.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", elm_scroll)
        time.sleep(random.uniform(1.5, 3.5))
        new_height = obj.BROWSER.execute_script("return arguments[0].scrollHeight", elm_scroll)

        if new_height == last_height:  # прокрутка списка не выполняется
            print("Достигнут конец списка.")
            break

        last_height = new_height
        scroll_attempts += 1

except Exception as e:
    print(f"Произошла ошибка: {e}")

# Задержка перед закрытием браузера
time.sleep(1100)
obj.BROWSER.quit()
