import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Dane użytkownika
VALID_USER = "standard_user"
VALID_PASS = "secret_sauce"

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()
    yield driver
    driver.quit()

def login(driver):
    driver.find_element(By.ID, "user-name").send_keys(VALID_USER)
    driver.find_element(By.ID, "password").send_keys(VALID_PASS)
    driver.find_element(By.ID, "login-button").click()
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "inventory_list"))
    )

def test_add_product_to_cart(driver):
    login(driver)

    # Kliknij "Add to cart" przy pierwszym produkcie
    driver.find_element(By.CLASS_NAME, "btn_inventory").click()

    # Sprawdź czy badge koszyka pokazuje "1"
    cart_badge = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "shopping_cart_badge"))
    )
    assert cart_badge.text == "1"

def test_remove_product_from_cart(driver):
    login(driver)

    # Dodaj produkt
    add_btn = driver.find_element(By.CLASS_NAME, "btn_inventory")
    add_btn.click()

    # Kliknij "Remove"
    remove_btn = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[text()='Remove']"))
    )
    remove_btn.click()

    # Sprawdź brak badge koszyka (czyli koszyk pusty)
    WebDriverWait(driver, 5).until_not(
        EC.presence_of_element_located((By.CLASS_NAME, "shopping_cart_badge"))
    )
