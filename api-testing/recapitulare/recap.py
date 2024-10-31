# VARIABILE
import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

a = 5
b = int(5.6)

print(a)
print(b)

PI = 3.14
print(int(PI))

print(bool(0))
print(bool(1))
print(bool(2))
print(bool(3))

text_1 = "Cerul este senin"

"""
cuvant: C e r u l _ e s t e _  s  e  n  i  n
 index: 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15
"""

print(text_1[::-1])
print(text_1)

print(text_1[::2])
print(text_1[::3])

print("Text 'de printat")

# COLECTII

# List
# mutabila, ordonata, duplicate, slicing
lista_1 = [1, "asd", True, 3.24]
lista_2 = []
lista_3 = list()

print(type(lista_1))
print(type(lista_2))
print(type(lista_3))

print(lista_1[::2])

# Tuple
# imutabil, ordonat, duplicate, slicing
tuplu_1 = ("s1", "s1", 4)
print(tuplu_1)

# Set
# nu este mutabil, nu este ordonat, nu permite duplicate, nici slicing
set_1 = {1, 7, 8, 1, 2, 2, 3, 4, 4, 5}
print(set_1)

# Dict
# Nu permite CHEI duplicate, permite VALORI duplicate
dict_1 = {
    "key_1": "val_1",
    "key_2": "val_1",
    "key_3": "val_1",
}

if a < b:
    print("a este mai mic decat b")
elif b < a:
    print("b este mai mic decat a")
else:
    print("a este egal cu b")

x = 1
while x < 10:
    print(x)
    x += 1  # x = x + 1

    if x == 5:
        break

print("-----------------")
for i in range(0, 11, 2):
    print(i)

print("-----------------")

for i in range(10, 0, -2):
    print(i)

for elem in lista_1:
    print(elem)


class Masina:
    roti = 4
    usi = 5


class VehiculElectric:
    putere = 250


class DaciaSpring(Masina, VehiculElectric):

    def __init__(self, cp):
        self.cp = cp

dacia_mea = DaciaSpring(200)


driver = webdriver.Chrome()
driver.get("http://google.com")

driver.find_element(By.ID, "L2AGLb").click()
driver.find_element(By.ID, "APjFqb").send_keys("emag" + Keys.ENTER)

time.sleep(5)

dropdown = Select(driver.find_element(By.ID, ""))

driver.implicitly_wait(5)

wait = WebDriverWait(driver, 10)
wait.until("...")

