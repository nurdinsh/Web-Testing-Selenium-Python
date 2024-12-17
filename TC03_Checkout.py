from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import unittest
import time
import baseLogin
import baseProduct
from page import elmen
from data import InformationsUser
from page import validasi

class testCheckout(unittest.TestCase):
    def setUp(self):
        service = Service(ChromeDriverManager().install())
        self.browser = webdriver.Chrome(service=service)
    def test_Checkout_success(self):
        driver = self.browser
        baseLogin.valid_Login(driver)
        UrlLogin = driver.current_url
        self.assertEqual(UrlLogin,validasi.URLLogin)
        baseProduct.AddProduct(driver)
        time.sleep(1)
        driver.find_element(By.XPATH,elmen.xPathCart).click()
        UrlCart = driver.current_url
        self.assertEqual(UrlCart,validasi.URLCart)
        time.sleep(1)
        driver.find_element(By.ID,elmen.btn_Checkout).click()
        UrlInformation = driver.current_url
        self.assertEqual(UrlInformation,validasi.URLInformation)
        time.sleep(1)
        driver.find_element(By.ID,elmen.IDFirtName).send_keys(InformationsUser.FirstName)
        time.sleep(1)
        driver.find_element(By.ID,elmen.IDLastName).send_keys(InformationsUser.LastName)
        time.sleep(1)
        driver.find_element(By.ID,elmen.IDPostalCode).send_keys(InformationsUser.PortalCode)
        time.sleep(1)
        driver.find_element(By.ID,elmen.IDContinue).click()
        UrlOverview = driver.current_url
        self.assertEqual(UrlOverview,validasi.URLOverview)
        time.sleep(1)
        driver.find_element(By.ID,elmen.IDFinish).click()
        UrlComplite = driver.current_url
        self.assertEqual(UrlComplite,validasi.URLComplit)
        time.sleep(2)

    def test_Checkout_Failed_Blank_Information(self):
        driver = self.browser
        baseLogin.valid_Login(driver)
        UrlLogin = driver.current_url
        self.assertEqual(UrlLogin,validasi.URLLogin)
        baseProduct.AddProduct(driver)
        time.sleep(1)
        driver.find_element(By.XPATH,elmen.xPathCart).click()
        UrlCart = driver.current_url
        self.assertEqual(UrlCart,validasi.URLCart)
        time.sleep(1)
        driver.find_element(By.ID,elmen.btn_Checkout).click()
        UrlInformation = driver.current_url
        self.assertEqual(UrlInformation,validasi.URLInformation)
        time.sleep(1)
        driver.find_element(By.ID,elmen.IDContinue).click()
        respones_date = driver.find_element(By.CSS_SELECTOR,elmen.CSSNameRequired).text
        self.assertIn(respones_date,validasi.FNemeRequired)
        time.sleep(2)

    def test_Checkout_Failed_Blank_FirstName(self):
        driver = self.browser
        baseLogin.valid_Login(driver)
        UrlLogin = driver.current_url
        self.assertEqual(UrlLogin,validasi.URLLogin)
        baseProduct.AddProduct(driver)
        time.sleep(1)
        driver.find_element(By.XPATH,elmen.xPathCart).click()
        UrlCart = driver.current_url
        self.assertEqual(UrlCart,validasi.URLCart)
        time.sleep(1)
        driver.find_element(By.ID,elmen.btn_Checkout).click()
        UrlInformation = driver.current_url
        self.assertEqual(UrlInformation,validasi.URLInformation)
        time.sleep(1)
        driver.find_element(By.ID,elmen.IDLastName).send_keys(InformationsUser.LastName)
        time.sleep(1)
        driver.find_element(By.ID,elmen.IDPostalCode).send_keys(InformationsUser.PortalCode)
        time.sleep(1)
        driver.find_element(By.ID,elmen.IDContinue).click()
        respones_date = driver.find_element(By.CSS_SELECTOR,elmen.CSSNameRequired).text
        self.assertIn(respones_date,validasi.FNemeRequired)
        time.sleep(2)

    def test_Checkout_Failed_Blank_LastName(self):
        driver = self.browser
        baseLogin.valid_Login(driver)
        UrlLogin = driver.current_url
        self.assertEqual(UrlLogin,validasi.URLLogin)
        baseProduct.AddProduct(driver)
        time.sleep(1)
        driver.find_element(By.XPATH,elmen.xPathCart).click()
        UrlCart = driver.current_url
        self.assertEqual(UrlCart,validasi.URLCart)
        time.sleep(1)
        driver.find_element(By.ID,elmen.btn_Checkout).click()
        UrlInformation = driver.current_url
        self.assertEqual(UrlInformation,validasi.URLInformation)
        time.sleep(1)
        driver.find_element(By.ID,elmen.IDFirtName).send_keys(InformationsUser.FirstName)
        time.sleep(1)
        driver.find_element(By.ID,elmen.IDPostalCode).send_keys(InformationsUser.PortalCode)
        time.sleep(1)
        driver.find_element(By.ID,elmen.IDContinue).click()
        respones_date = driver.find_element(By.CSS_SELECTOR,elmen.CSSNameRequired).text
        self.assertIn(respones_date,validasi.LNameRequired)
        time.sleep(2)

    def test_Checkout_Failed_Blank_PortalCode(self):
        driver = self.browser
        baseLogin.valid_Login(driver)
        UrlLogin = driver.current_url
        self.assertEqual(UrlLogin,validasi.URLLogin)
        baseProduct.AddProduct(driver)
        time.sleep(1)
        driver.find_element(By.XPATH,elmen.xPathCart).click()
        UrlCart = driver.current_url
        self.assertEqual(UrlCart,validasi.URLCart)
        time.sleep(1)
        driver.find_element(By.ID,elmen.btn_Checkout).click()
        UrlInformation = driver.current_url
        self.assertEqual(UrlInformation,validasi.URLInformation)
        time.sleep(1)
        driver.find_element(By.ID,elmen.IDFirtName).send_keys(InformationsUser.FirstName)
        time.sleep(1)
        driver.find_element(By.ID,elmen.IDLastName).send_keys(InformationsUser.LastName)
        time.sleep(1)
        driver.find_element(By.ID,elmen.IDContinue).click()
        respones_date = driver.find_element(By.CSS_SELECTOR,elmen.CSSNameRequired).text
        self.assertIn(respones_date,validasi.PostalRequire)
        time.sleep(2)

    def test_Checkout_Failed_Blank_FirstName_and_LastName(self):
        driver = self.browser
        baseLogin.valid_Login(driver)
        UrlLogin = driver.current_url
        self.assertEqual(UrlLogin,validasi.URLLogin)
        baseProduct.AddProduct(driver)
        time.sleep(1)
        driver.find_element(By.XPATH,elmen.xPathCart).click()
        UrlCart = driver.current_url
        self.assertEqual(UrlCart,validasi.URLCart)
        time.sleep(1)
        driver.find_element(By.ID,elmen.btn_Checkout).click()
        UrlInformation = driver.current_url
        self.assertEqual(UrlInformation,validasi.URLInformation)
        time.sleep(1)
        driver.find_element(By.ID,elmen.IDPostalCode).send_keys(InformationsUser.PortalCode)
        time.sleep(1)
        driver.find_element(By.ID,elmen.IDContinue).click()
        respones_date = driver.find_element(By.CSS_SELECTOR,elmen.CSSNameRequired).text
        self.assertIn(respones_date,validasi.FNemeRequired)
        time.sleep(2)
    
    def test_Checkout_Failed_Blank_FirstName_and_PostalCode(self):
        driver = self.browser
        baseLogin.valid_Login(driver)
        UrlLogin = driver.current_url
        self.assertEqual(UrlLogin,validasi.URLLogin)
        baseProduct.AddProduct(driver)
        time.sleep(1)
        driver.find_element(By.XPATH,elmen.xPathCart).click()
        UrlCart = driver.current_url
        self.assertEqual(UrlCart,validasi.URLCart)
        time.sleep(1)
        driver.find_element(By.ID,elmen.btn_Checkout).click()
        UrlInformation = driver.current_url
        self.assertEqual(UrlInformation,validasi.URLInformation)
        time.sleep(1)
        driver.find_element(By.ID,elmen.IDLastName).send_keys(InformationsUser.LastName)
        time.sleep(1)
        driver.find_element(By.ID,elmen.IDContinue).click()
        respones_date = driver.find_element(By.CSS_SELECTOR,elmen.CSSNameRequired).text
        self.assertIn(respones_date,validasi.FNemeRequired)
        time.sleep(2)

    def test_Checkout_Failed_Blank_LastName_and_PostalCode(self):
        driver = self.browser
        baseLogin.valid_Login(driver)
        UrlLogin = driver.current_url
        self.assertEqual(UrlLogin,validasi.URLLogin)
        baseProduct.AddProduct(driver)
        time.sleep(1)
        driver.find_element(By.XPATH,elmen.xPathCart).click()
        UrlCart = driver.current_url
        self.assertEqual(UrlCart,validasi.URLCart)
        time.sleep(1)
        driver.find_element(By.ID,elmen.btn_Checkout).click()
        UrlInformation = driver.current_url
        self.assertEqual(UrlInformation,validasi.URLInformation)
        time.sleep(1)
        driver.find_element(By.ID,elmen.IDFirtName).send_keys(InformationsUser.FirstName)
        time.sleep(1)
        driver.find_element(By.ID,elmen.IDContinue).click()
        respones_date = driver.find_element(By.CSS_SELECTOR,elmen.CSSNameRequired).text
        self.assertIn(respones_date,validasi.LNameRequired)
        time.sleep(2)

    def test_Checkout_Failed_Cencel(self):
        driver = self.browser
        baseLogin.valid_Login(driver)
        UrlLogin = driver.current_url
        self.assertEqual(UrlLogin,validasi.URLLogin)
        baseProduct.AddProduct(driver)
        time.sleep(1)
        driver.find_element(By.XPATH,elmen.xPathCart).click()
        UrlCart = driver.current_url
        self.assertEqual(UrlCart,validasi.URLCart)
        time.sleep(1)
        driver.find_element(By.ID,elmen.btn_Checkout).click()
        UrlInformation = driver.current_url
        self.assertEqual(UrlInformation,validasi.URLInformation)
        time.sleep(1)
        driver.find_element(By.ID,elmen.IDFirtName).send_keys(InformationsUser.FirstName)
        time.sleep(1)
        driver.find_element(By.ID,elmen.IDLastName).send_keys(InformationsUser.LastName)
        time.sleep(1)
        driver.find_element(By.ID,elmen.IDPostalCode).send_keys(InformationsUser.PortalCode)
        time.sleep(1)
        driver.find_element(By.XPATH,elmen.xPathCencel).click()
        UrlCart = driver.current_url
        self.assertEqual(UrlCart,validasi.URLCart)
        time.sleep(2)

    def test_Checkout_Failed_Continue_Shopping(self):
        driver = self.browser
        baseLogin.valid_Login(driver)
        UrlLogin = driver.current_url
        self.assertEqual(UrlLogin,validasi.URLLogin)
        baseProduct.AddProduct(driver)
        time.sleep(1)
        driver.find_element(By.XPATH,elmen.xPathCart).click()
        UrlCart = driver.current_url
        self.assertEqual(UrlCart,validasi.URLCart)
        time.sleep(1)
        driver.find_element(By.ID,elmen.IDContinueShopping).click()
        UrlLogin = driver.current_url
        self.assertEqual(UrlLogin,validasi.URLLogin)
        time.sleep(2)


    def tearDown(self):
        self.browser.quit()

if __name__ == "__main__":
    unittest.main()

