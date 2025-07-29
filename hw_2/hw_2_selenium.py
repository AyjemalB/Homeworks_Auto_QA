from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.firefox import GeckoDriverManager
from time import sleep

# Настройка Firefox
options = Options()

# Инициализация драйвера
service = Service(GeckoDriverManager().install())
driver = webdriver.Firefox(service=service, options=options)

try:
    # Открываем сайт
    driver.get("https://itcareerhub.de/ru")
    wait = WebDriverWait(driver, 10)

    # Найти заголовок
    header = driver.find_element(By.XPATH, "//div[@class='tn-atom' and text()='Способы оплаты обучения']")

    # Найти родительский контейнер секции
    section = header.find_element(By.XPATH, "./ancestor::div[contains(@class, 't396')]")

    # Задержка перед скриншотом
    sleep(10)

    # Сделать скриншот только этой секции
    section.screenshot("payment_section.png")

    print("Скриншот сделан!")

except Exception as e:
    print(f"Произошла ошибка: {e}")

# Закрытие драйвера
finally:
    driver.quit()
