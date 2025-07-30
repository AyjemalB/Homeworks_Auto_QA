import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

@pytest.fixture
def browser():
    options = Options()
    options.add_argument("--headless")  # Для запуска без открытия окна браузера
    service = Service()
    driver = webdriver.Chrome(service=service, options=options)
    yield driver
    driver.quit()

def test_text_input_button(browser):
    url = "http://uitestingplayground.com/textinput"
    browser.get(url)

    # Находим поле ввода и вводим текст
    input_field = browser.find_element(By.ID, "newButtonName")
    input_field.send_keys("ITCH")

    # Находим синюю кнопку и нажимаем
    button = browser.find_element(By.ID, "updatingButton")
    button.click()

    # Проверяем, что текст на кнопке изменился на "ITCH"
    assert button.text == "ITCH", f"Ожидался текст 'ITCH', но получен '{button.text}'"
