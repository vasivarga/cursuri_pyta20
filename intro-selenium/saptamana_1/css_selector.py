import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Firefox()

driver.get("https://formy-project.herokuapp.com/form")

# driver.find_element(By.ID, "first-name")

#Cautam elementul dupa id in diferite moduri
driver.find_element(By.CSS_SELECTOR, "#first-name").send_keys("Automation")
driver.find_element(By.CSS_SELECTOR, "[id='first-name']").send_keys("Testing")
driver.find_element(By.CSS_SELECTOR, "input[id='first-name']")

#Cautam acelasi element dupa pereche de atribut=valoare
driver.find_element(By.CSS_SELECTOR, "input[placeholder='Enter first name']")

#Cautam un element input cu id-ul last-name care are un parinte div ( > - relatia copil-parinte)
driver.find_element(By.CSS_SELECTOR, "div > input#last-name").send_keys("PYTA20")

#Pornim din elementul form > cu copil div > cu al 3-lea copil div (nth-of-type) > care are un copil input
driver.find_element(By.CSS_SELECTOR, "form > div > div:nth-of-type(3) > input").send_keys("QA Engineer")

driver.find_element(By.CSS_SELECTOR, "input[value='radio-button-1']").click()

driver.find_element(By.CSS_SELECTOR, "input[value='checkbox-1']").click()

# Pentru a selecta optiuni de pe un dropdown (select in html), vom folosi clasa Select din selenium
dropdown = Select(driver.find_element(By.CSS_SELECTOR, "#select-menu"))

#Selectam dupa textul de pe optiune
dropdown.select_by_visible_text("0-1")
time.sleep(1)

#Selectam dupa ordinea optiunii
dropdown.select_by_index(3)
time.sleep(1)

#Selectam dupa atributul value (care la option este obligatoriu)
dropdown.select_by_value("4")


"""
driver.find_element()
- primeste 2 argumente
- primul arg: By - specificam dupa ce tip de selector urmeaza sa cautam
- al doilea arg: valoarea selectorului
- daca gaseste element in pagina: retuneaza un obiect din clasa WebElement
- daca nu gaseste un element: NoSuchElementException - selectorul meu e valid, 
    dar nu a existat pana in momentul cautarii un element cu acel selector in pagina
"""

"""
driver.find_elements()
- primeste 2 argumente
- primul argument - specificam dupa ce tip de selector urmeaza sa cautam
- al doilea argument - valoarea selectorului dupa care cautam TOATE elementele din pagina
- daca gaseste elemente in pagina: retuneaza o lista cu elemente, toate de tipul WebElement
- daca nu gaseste elemente in pagina: ne va returna o lista goala!!!
"""
lista_elemente_gasite = driver.find_elements(By.CSS_SELECTOR, ".form-control")
print(len(lista_elemente_gasite))

lista_2 = driver.find_elements(By.CSS_SELECTOR, ".nuexista")
print(len(lista_2))

for element in lista_elemente_gasite:
    print(element.get_attribute("type"))
    print(element.get_attribute("value"))

    if element.get_attribute("type") == "text":
        element.clear()

    print("-------------------------")

# Caz negativ - cand elementul nu exista primim NoSuchElementException
# driver.find_element(By.CSS_SELECTOR, ".nuexista")


time.sleep(3)
driver.quit()