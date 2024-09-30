# Test case 1 - Happy flow log in
import random
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# deschid browserul
driver = webdriver.Firefox()

# navighez la site
driver.get("https://magento.softwaretestingboard.com/customer/account/create/")
# completez firstName
driver.find_element(By.XPATH, "//input[@id='firstname']").send_keys("Py")

# completez lastName
driver.find_element(By.XPATH, "//input[@id='lastname']").send_keys("Ta")

# completez email (cum fac sa nu ma repet?)
random_email = f"pyta20@itfactory{random.randint(99999, 9999999999999)}.ro"
driver.find_element(By.XPATH, "//input[@id='email_address']").send_keys(random_email)

# completez parola
# XPATH: input care contine in atributul @data-validate valoarea 'validate-customer-password'
password = "Pyta2024"
driver.find_element(By.XPATH, "//input[contains(@data-validate, 'validate-customer-password')]").send_keys(password)

# confirm parola
driver.find_element(By.XPATH, "//input[@name='password_confirmation']").send_keys(password)

# click pe create account
# cautare dupa textul de pe element - doar de pe element: text()
# cautare dupa textul de pe element - in toate sub-elementele: .
driver.find_element(By.XPATH, "//button[.='Create an Account']").click()


# REZULTATE ASTEPTATE
# - apare mesaj?
# - sunt redirectionat pe alta pagina?
# - imi apare un element nou?

# 1 - linkul nu mai contine path-ul '/create'
# 2 - mesajul cu textul 'Thank you for registering with Main Website Store.' e afisat
time.sleep(1)
link_creare_cont = "https://magento.softwaretestingboard.com/customer/account/create/"
link_curent = driver.current_url

assert '/create' not in link_curent, "'/create' path is in the current URL"
success_message = driver.find_element(By.XPATH, "//div[text()='Thank you for registering with Main Website Store.']")

assert success_message.is_displayed(), "Success message is not displayed"
driver.quit()