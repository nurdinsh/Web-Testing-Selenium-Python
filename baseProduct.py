from selenium.webdriver.common.by import By
from page import elmen
import time

def AddProduct(driver):
    time.sleep(1)
    driver.find_element(By.ID,elmen.IDadd).click()
    time.sleep(1)

