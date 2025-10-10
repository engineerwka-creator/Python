import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#C:\Users\engin\Downloads\chrome-win64\chrome-win64
#https://www.saucedemo.com/inventory.html

@pytest.fixture
def driver():
    # Uruchomienie przeglądarki
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")
    yield driver
    driver.quit()

def test_login_sauce_demo_OK(driver):
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    wait = WebDriverWait(driver, 10)
    title = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "title")))
    assert "inventory" in driver.current_url
    assert title.text == "Products"


def test_login_sauce_demo_NOK(driver):
    driver.find_element(By.ID, "user-name").send_keys("standard")
    driver.find_element(By.ID, "password").send_keys("secret")
    driver.find_element(By.ID, "login-button").click()
    wait = WebDriverWait(driver, 10)
    error_msg = wait.until(EC.presence_of_element_located((By.XPATH, "//h3[@data-test='error']"))).text
    assert "Epic sadface" in error_msg
    # assert "inventory" in driver.current_url
    # assert driver.find_element(By.CLASS_NAME, "title").text == "Products"

