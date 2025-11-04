# 🧩 Co to jest Selenium
# Selenium to biblioteka (framework) do automatyzacji przeglądarki internetowej.
# Pozwala Twojemu programowi sterować przeglądarką tak, jak człowiek — klikać przyciski, wypełniać formularze, przewijać strony, pobierać dane itd.
#
# | Metoda                                               | Opis                | Przykład                                                 |
# | ---------------------------------------------------- | ------------------- | -------------------------------------------------------- |
# | `find_element(By.ID, "id")`                          | znajdź po ID        | `driver.find_element(By.ID, "username")`                 |
# | `find_element(By.NAME, "name")`                      | po atrybucie `name` | `driver.find_element(By.NAME, "q")`                      |
# | `find_element(By.CLASS_NAME, "class")`               | po klasie CSS       | `driver.find_element(By.CLASS_NAME, "btn")`              |
# | `find_element(By.TAG_NAME, "tag")`                   | po znaczniku HTML   | `driver.find_element(By.TAG_NAME, "h1")`                 |
# | `find_element(By.LINK_TEXT, "tekst linku")`          | po treści linku     | `driver.find_element(By.LINK_TEXT, "Login")`             |
# | `find_element(By.XPATH, "//input[@type='text']")`    | po ścieżce XPath    | `driver.find_element(By.XPATH, "//button[text()='OK']")` |
# | `find_element(By.CSS_SELECTOR, "div.class > input")` | po selektorze CSS   | `driver.find_element(By.CSS_SELECTOR, "#id > input")`    |
#
# | Działanie                  | Kod                              |
# | -------------------------- | -------------------------------- |
# | Kliknięcie                 | `element.click()`                |
# | Wpisanie tekstu            | `element.send_keys("tekst")`     |
# | Wciśnięcie klawisza Enter  | `element.send_keys(Keys.RETURN)` |
# | Pobranie tekstu z elementu | `element.text`                   |
# | Pobranie wartości atrybutu | `element.get_attribute("href")`  |
#
# driver.back()         wróć do poprzedniej strony | driver.save_screenshot                              zrzut.png
# driver.forward()      przejdź do następnej       | driver.switch_to.window(driver.window_handles[1])   przełącz na drugą kartę
# driver.refresh()      odśwież                    | driver.close()                                      zamknij aktualną kartę
# driver.get("URL")     otwórz nową stronę         | driver.quit()                                       zamknij całą przeglądarkę


import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

#from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.support import expected_conditions as EC


# Uruchomienie Chrome
driver = webdriver.Chrome()

# Otwórz stronę
driver.get("https://www.yahoo.com")
time.sleep (10)

agree_button = driver.find_element(By.NAME, "agree")
agree_button.click()
time.sleep(60)
# print(alert.text)
# alert.accept()   # OK
# alert.dismiss()  # Anuluj

search_box = driver.find_element(By.ID, "ybar-sbq")
search_box.send_keys("Selenium Python")
search_box.send_keys(Keys.RETURN)

time.sleep(600)
print(driver.title)
driver.quit()