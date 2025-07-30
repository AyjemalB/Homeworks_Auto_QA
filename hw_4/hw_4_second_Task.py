import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_loading_images(browser):
    url = "https://bonigarcia.dev/selenium-webdriver-java/loading-images.html"
    browser.get(url)

    # Ждём появления как минимум 3 изображений
    WebDriverWait(browser, 15).until(
        lambda driver: len(driver.find_elements(By.CSS_SELECTOR, "img")) >= 4
    )

    images = browser.find_elements(By.CSS_SELECTOR, "img")

    # Проверка безопасного доступа
    assert len(images) >= 3, f"Недостаточно изображений: {len(images)}"
    third_image_alt = images[3].get_attribute("alt")
    assert third_image_alt == "award", f"Ожидался 'award', но получено '{third_image_alt}'"
