import pytest
import time
from selenium import webdriver
#C:\Users\engin\Downloads\chrome-win64\chrome-win64


def test_open_google():
    driver = webdriver.Chrome()
    driver.get("https://www.google.com")
    time.sleep(5)
    driver.quit()
