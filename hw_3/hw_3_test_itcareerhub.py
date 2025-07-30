import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--headless")  # Для запуска без открытия окна браузера
    options.add_argument("--disable-logging")
    options.add_argument("--log-level=3")
    service = Service()  # Использует установленный chromedriver
    driver = webdriver.Chrome(service=service, options=options)
    driver.get("https://itcareerhub.de/ru")
    yield driver
    driver.quit()

def test_main_page_elements(driver):
    # Логотип
    assert driver.find_element(By.CSS_SELECTOR, "img[alt='IT Career Hub']")

    # Ссылки
    expected_links = ["Программы", "Способы оплаты", "Новости", "О нас", "Отзывы"]
    for link_text in expected_links:
        assert driver.find_element(By.LINK_TEXT, link_text)

    # Кнопки переключения языка
    assert driver.find_element(By.XPATH, "//a[@href='/ru' and contains(text(), 'ru')]")
    assert driver.find_element(By.XPATH, "//a[@href='/' and contains(text(), 'de')]")


def test_phone_icon_click(driver):
    wait = WebDriverWait(driver, 10)

    # Ждем, пока кнопка будет кликабельна
    phone_icon = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[href='#popup:form-tr3'][role='button']")))

    # Скроллим к элементу, чтобы не было перекрытий
    driver.execute_script("arguments[0].scrollIntoView(true);", phone_icon)

    # Пытаемся кликнуть, если не получится — кликаем через JS
    try:
        phone_icon.click()
    except Exception:
        driver.execute_script("arguments[0].click();", phone_icon)

    # Проверяем, что появится нужный текст
    text_element = wait.until(EC.visibility_of_element_located(
        (By.XPATH, "//*[contains(text(), 'Если вы не дозвонились, заполните форму на сайте. Мы свяжемся с вами')]")))
    assert text_element is not None


