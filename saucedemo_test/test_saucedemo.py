from selenium import webdriver
import time
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.overview_page import OverviewPage

def test_total_price():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/") # Открытие сайта

    # Инициализация страницы входа
    login = LoginPage(driver)
    # Вход с логином и паролем
    login.login("standard_user", "secret_sauce")

    inventory = InventoryPage(driver) # Инициализация страницы товаров
    inventory.add_items_to_cart() # Добавление товаров в корзину
    inventory.go_to_cart() # Переход в корзину

    cart = CartPage(driver) # Инициализация страницы корзины
    cart.click_checkout() # Переход к оформлению заказа

    checkout = CheckoutPage(driver) # Инициализация страницы оформления
    checkout.fill_information("John", "Doe", "12345") # Ввод личной информации

    overview = OverviewPage(driver) # Инициализация страницы обзора заказа
    total_text = overview.get_total_price()  # Получение текста с итоговой суммой
    total = float(total_text.replace("Total: $", ""))  # Преобразование суммы в число

    # Проверка соответствия суммы ожиданиям
    assert total == 58.29, f"Expected total $58.29, but got ${total}"

    driver.quit()
