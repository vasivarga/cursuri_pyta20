import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# Instantiere webdriver de tip Firefox. Variabila driver este de tip WebDriver
driver = webdriver.Firefox()

# driver.get() - navigare catre un site
driver.get("https://the-internet.herokuapp.com/login")

# driver.find_element() - gaseste un element dupa un locator dat
# By - startegie de cautare (ID, CLASS_NAME, NAME, etc)

# Cautare dupa ID
username_textbox = driver.find_element(By.ID, "username")
username_textbox.send_keys("tomsmith")
username_textbox.clear()

time.sleep(1)
# dupa refresh elementele din pagina sunt reincarcate - au referinte noi, cele vechi nu mai sunt valabile
driver.refresh()

# pentru a putea interactiona din nou cu acelasi element trebuie sa-l gasim iar,
# altfel primim exceptie de tipul StaleElementReferenceException
username_textbox_2 = driver.find_element(By.ID, "username")
username_textbox_2.send_keys("tomsmith")
username_textbox_2.clear()

# Alternativa daca trebuie sa gasim acelasi element de mai multe ori:
# declaram o functie care scrie pe textboxul de username
def set_username(text):
    driver.find_element(By.ID, "username").send_keys(text)

# Apelam functia ori de cate ori avem nevoie
set_username("tomsmith")

# COD CU EXCEPTIE: incercam sa gasim un element care nu exista - aici primim NoSuchElementException:
# driver.find_element(By.ID, "id_inexistent")

# Cautare dupa NAME
driver.find_element(By.NAME, "password").send_keys("SuperSecretPassword!")

# Cautare dupa CLASS_NAME (o singura clasa)
driver.find_element(By.CLASS_NAME, "radius").click()

# Cautare dupa LINK_TEXT & PARTIAL_LINK_TEXT
assert driver.find_element(By.LINK_TEXT, "Elemental Selenium").is_displayed()
assert driver.find_element(By.PARTIAL_LINK_TEXT, "Elemental").is_displayed()

"""
########### assert ###########

assert este sintaxa care evalueaza o expresie 
- nu face nimic daca expresia este adevarata, trece mai departe
- returneaza o exceptie tip AssertionError in cazul in care expresia nu este adevarata, se opreste programul

Practic, in testare automata, un assert este cel care decide daca testul e "trecut" sau "picat" (passed sau failed) 
"""

# assert False, "Eroare, expresia verificata a returnat Fals"

print("Am trecut de assert")
time.sleep(5)

# driver.find_element(By.LINK_TEXT, "Dropdown")
# driver.find_element(By.LINK_TEXT, "Form Authentication")
# driver.find_element(By.LINK_TEXT, "Shadow DOM")
#
# driver.find_element(By.PARTIAL_LINK_TEXT, "Notifica")
#
# driver.find_element(By.NAME, "login")
# driver.find_element(By.NAME, "username")
# driver.find_element(By.NAME, "password")
#
# driver.find_element(By.TAG_NAME, "button")

driver.quit()


