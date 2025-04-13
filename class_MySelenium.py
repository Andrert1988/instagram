
from selenium import webdriver  # Для создания браузера
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


class MySelenium:

    BROWSER = None  # Переменная содержащая Браузер

    # Тема 1. Создание браузера (headless: Скрыть окно) (profile: Профиль браузера)
    def create_browser(self, headless=False, profile=None):

        # Опции Браузера
        options = webdriver.ChromeOptions()  # Создание дополнительных ОПЦИЙ для браузера.

        # Опция для создания браузера с профилем
        if profile is not None:
            options.add_argument("user-data-dir={}".format(profile))

        options.add_argument("--window-size={},{}".format(1100, 900))  # Размер окна
        options.add_argument("--window-position={},{}".format(50, 50))  # Позиция окна

        # Создание Браузера
        self.BROWSER = webdriver.Chrome(options=options)




