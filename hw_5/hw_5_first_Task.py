import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def driver():
    service = Service()
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    driver = webdriver.Chrome(service=service, options=options)
    yield driver
    driver.quit()

def test_iframe_text(driver):
    # Открыть страницу
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/iframes.html")

    # Найти все iframe'ы
    iframes = driver.find_elements(By.TAG_NAME, "iframe")

    # Перебрать iframe'ы и искать нужный текст
    target_text = "semper posuere integer et senectus justo curabitur."
    found = False

    for iframe in iframes:
        # Переключиться в него (Найдено iframe)
        driver.switch_to.frame(iframe)
        try:
            # Ожидание появления элемента с нужным текстом
            WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.XPATH, f"//*[@id=contains(text(), '{target_text}')]"))
            )
            found = True
            break
        except:
            pass
        finally:
            # Вернуться в основной контекст
            driver.switch_to.default_content()

    assert found, f"Текст '{target_text}' не найден ни в одном iframe"
