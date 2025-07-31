import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import TimeoutException

@pytest.fixture
def driver():
    service = Service(ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=service, options=options)
    driver.get("https://www.globalsqa.com/demo-site/draganddrop/")
    # закрываем куки-баннер
    try:
        consent_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button.fc-button.fc-cta-consent"))
        )
        consent_button.click()
    except TimeoutException:
        print("Баннер не найден")
    yield driver
    driver.quit()


def test_drag_and_drop_image(driver):
    wait = WebDriverWait(driver, 10)

    # iframe с демо
    iframe = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "iframe.demo-frame")))
    driver.switch_to.frame(iframe)

    # ждем хотя бы одного изображения
    gallery_images = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#gallery > li")))

    # захватываем первое изображение
    source = gallery_images[0]

    # находим корзину
    trash = driver.find_element(By.ID, "trash")

    # Выполняем перетаскивание
    ActionChains(driver).click_and_hold(source).move_to_element(trash).release().perform()

    # проверяем наличие изображения в корзине
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#trash > ul > li")))

    # получаем количество изображений в корзине и галереи
    trash_items = driver.find_elements(By.CSS_SELECTOR, "#trash > ul > li")
    gallery_items = driver.find_elements(By.CSS_SELECTOR, "#gallery > li")

    assert len(trash_items) == 1, "В корзине должно быть 1 изображение"
    assert len(gallery_items) == 3, "В галерее должно остаться 3 изображения"