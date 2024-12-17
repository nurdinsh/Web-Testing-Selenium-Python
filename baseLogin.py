
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from page import elmen #Element web
from page import Url
from data import inputValid
import time


def valid_Login(driver): 
        
        driver.get(Url.base_url)
        driver.maximize_window()
        WebDriverWait(driver,10).until(
                EC.presence_of_element_located((By.ID,elmen.IDusername))
        )
        time.sleep(1)
        driver.find_element(By.ID,elmen.IDusername).send_keys(inputValid.username)
        time.sleep(1)
        driver.find_element(By.ID,elmen.IDpassword).send_keys(inputValid.password)
        time.sleep(1)
        driver.find_element(By.ID,elmen.btn_login).click()

        #verifikasi
        #response = driver.find_element(By.CLASS_NAME,elmen.title).text
        #self.assertIn(validasi.product,response)