import unittest
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By #Fine element
from webdriver_manager.chrome import ChromeDriverManager 
from page import elmen #Element web
from page import validasi
from page import Url
from data import inputInvalid
from data import inputValid

class TestLogin(unittest.TestCase):

    def setUp(self):
        #self.browser = webdriver.Chrome(ChromeDriverManager().install())
        service = Service(ChromeDriverManager().install())
        self.browser = webdriver.Chrome(service=service)

        #Verify Login Successfully
    def test_a_Login_Successfully(self):  
        #Steps
        driver = self.browser #Open web browser
        driver.get(Url.base_url) #Open website
        time.sleep(2)
        driver.find_element(By.ID,elmen.IDusername).send_keys(inputValid.username) #Input email
        time.sleep(1)
        driver.find_element(By.ID,elmen.IDpassword).send_keys(inputValid.password) #Input password
        time.sleep(1)
        driver.find_element(By.ID,elmen.btn_login).click()
        time.sleep(1)
        #Validasi
        response_data = driver.find_element(By.CLASS_NAME,elmen.title).text
        self.assertIn(validasi.product, response_data)

        #Verify Login Failed Invalid Username and Password
    def test_b_Login_Failed_Invalid_Username_and_Password(self):
        #Steps
        driver = self.browser
        driver.get(Url.base_url)
        time.sleep(2)
        driver.find_element(By.ID,elmen.IDusername).send_keys(inputInvalid.username) #Input invalid emali
        time.sleep(1)
        driver.find_element(By.ID,elmen.IDpassword).send_keys(inputInvalid.password) #Input invalid pasword
        time.sleep(1)
        driver.find_element(By.ID,elmen.btn_login).click()
        time.sleep(1)
        #Validasi
        response_date = driver.find_element(By.XPATH,elmen.xPathInvalid).text
        self.assertEqual(response_date,validasi.InvalidUserandPassword)
        time.sleep(2)
    
        #Verify Login Failed Invalid Username
    def test_c_Login_Failed_Invalid_Username(self):
        #Steps
        driver = self.browser
        driver.get(Url.base_url)
        time.sleep(2)
        driver.find_element(By.ID,elmen.IDusername).send_keys(inputInvalid.username) #Input invalid email
        time.sleep(1)
        driver.find_element(By.ID,elmen.IDpassword).send_keys(inputValid.password) #Input password
        time.sleep(1)
        driver.find_element(By.ID,elmen.btn_login).click()
        #Validasi
        response_data = driver.find_element(By.XPATH,elmen.xPathInvalid).text
        self.assertEqual(response_data,validasi.InvalidUserandPassword)
        time.sleep(2)

        #Verify Login Failed Invalid Password
    def test_d_Login_Failed_Invalid_Password(self):
        #Steps
        driver = (self.browser)
        driver.get(Url.base_url)
        time.sleep(2)
        driver.find_element(By.ID,elmen.IDusername).send_keys(inputValid.username) #Input email
        time.sleep(1)
        driver.find_element(By.ID,elmen.IDpassword).send_keys(inputInvalid.password) #Input invalid password
        time.sleep(1)
        driver.find_element(By.ID,elmen.btn_login).click()
        #Verivikasi
        response_date = driver.find_element(By.XPATH,elmen.xPathInvalid).text
        self.assertEqual(response_date,validasi.InvalidUserandPassword)
        time.sleep(2)

        #Verify Login Failed Blank Field
    def test_e_Login_Failed_Blank_Field(self):
        #Steps
        driver = (self.browser)
        driver.get(Url.base_url)
        time.sleep(2)
        driver.find_element(By.ID,elmen.btn_login).click()
        #Verivikasi
        responde_date = driver.find_element(By.XPATH,elmen.xPathInvalid).text
        self.assertEqual(responde_date,validasi.BlankUsername)
        time.sleep(2)

        #Verify Login Failed Blank Username
    def test_f_Login_Failed_Blank_Username(self):
        #Steps
        driver = (self.browser)
        driver.get(Url.base_url)
        time.sleep(2)
        driver.find_element(By.ID,elmen.IDpassword).send_keys(inputValid.password) #Input password
        time.sleep(1)
        driver.find_element(By.ID,elmen.btn_login).click()
        #Verivikasi
        response_date = driver.find_element(By.XPATH,elmen.xPathInvalid).text
        self.assertEqual(response_date,validasi.BlankUsername)
        time.sleep(2)

        #Verify Login Failed Blank Password
    def test_g_Failed_Login_Blank_Password(self):
        #Steps
        driver = (self.browser)
        driver.get(Url.base_url)
        time.sleep(2)
        driver.find_element(By.ID,elmen.IDusername).send_keys(inputValid.username) #Input username
        time.sleep(1)
        driver.find_element(By.ID,elmen.btn_login).click()
        #Verivikasi
        response_date = driver.find_element(By.XPATH,elmen.xPathInvalid).text
        self.assertEqual(response_date,validasi.BlankPassword)
        time.sleep(2)

    def tearDown(self):
        self.browser.quit()

if __name__ == "__main__":
    unittest.main()