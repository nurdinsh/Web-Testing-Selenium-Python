import unittest
import time
#import os
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
#from selenium.common.exceptions import TimeoutException, NoSuchAttributeException
#from selenium.webdriver.common.action_chains import ActionChains
#from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import baseLogin
import baseProduct
from page import validasi
from page import elmen
from data import SelectCatagory

class TestProduct (unittest.TestCase):
    def setUp(self):
        service = Service(ChromeDriverManager().install())
        self.browser = webdriver.Chrome(service=service)

    def test_Add_Product_to_Card(self):
        driver = self.browser
        baseLogin.valid_Login(driver)
        time.sleep(2)
        driver.find_element(By.ID,elmen.IDadd).click()
        time.sleep(2)
        
        #verifikasi
        response_date = driver.find_element(By.ID,elmen.IDremove).text
        self.assertIn(response_date,validasi.remove)
        time.sleep(2)

    def test_Remove_Product_in_Dashboard(self):
        driver = self.browser
        baseLogin.valid_Login(driver)
        baseProduct.AddProduct(driver)
        driver.find_element(By.ID,elmen.IDremove).click()
        time.sleep(1)

        #verifikasi
        respone_date = driver.find_element(By.ID,elmen.IDadd).text
        self.assertEqual(respone_date,validasi.AddProduct)
        time.sleep(1)
    
    def test_Remove_Product_in_Cart(self):
        driver = self.browser
        baseLogin.valid_Login(driver)
        baseProduct.AddProduct(driver)
        driver.find_element(By.XPATH,elmen.xPathCart).click()
        time.sleep(2)
        driver.find_element(By.ID,elmen.IDremove).click()
        time.sleep(2)

        #verifikasi
        respone_date = driver.find_element(By.XPATH,elmen.xPathDesc).text
        self.assertIn(respone_date,validasi.Descripsi)

    def test_View_Product_Picture(self):
        driver = self.browser
        baseLogin.valid_Login(driver)
        time.sleep(1) 
        driver.find_element(By.ID,elmen.IDProductImage).click()
        time.sleep(2)    

        #verifikasi
        respone_date = driver.find_element(By.XPATH,elmen.xPathImageProduct).text
        self.assertIn(respone_date,validasi.nameProduct)

    def test_Product_Filter_by(self):
        driver = self.browser
        baseLogin.valid_Login(driver)
        time.sleep(1)

        element_dropdown = driver.find_element(By.XPATH,elmen.xPathSelect)
        select = Select(element_dropdown)
        #select.select_by_visible_text(SelectCatagory.catagory)

        allOption = select.options
        for option in allOption:
         #print(option.text)
         if option.text == SelectCatagory.catagory:
             option.click()
             break
        time.sleep(1)

        #verifikasi
    
    
    def tearDown(self):
        self.browser.quit()






if __name__ == "__main__":
    unittest.main()

