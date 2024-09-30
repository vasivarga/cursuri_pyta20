import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

driver = webdriver.Firefox()
driver.get("https://primeng.org/dropdown")

dropdown = driver.find_element(By.ID, "pn_id_2")
# dropdown.click()
#
# time.sleep(1)
# dropdown.find_element(By.XPATH, "//p-dropdownitem//li[.='New York']").click()

def select_dropdown_option(dropdown: WebElement, text):
    dropdown.click()
    time.sleep(1)
    dropdown.find_element(By.XPATH, f"//p-dropdownitem//li[.='{text}']").click()


select_dropdown_option(dropdown, "New York")
select_dropdown_option(dropdown, "Rome")
select_dropdown_option(dropdown, "London")




time.sleep(3)
driver.quit()