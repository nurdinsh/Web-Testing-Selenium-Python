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
from page import Url

class TestLogout(unittest.TestCase):
    def setUp(self):
        service = Service(ChromeDriverManager().install())
        self.browser = webdriver.Chrome(service=service)
    def test_Checkout_success(self):
        driver = self.browser
        baseLogin.valid_Login(driver)
        UrlLogin = driver.current_url
        self.assertEqual(UrlLogin,validasi.URLLogin)
        time.sleep(1)
        driver.find_element(By.ID,elmen.IDBurgerMenu).click()
        time.sleep(1)
        driver.find_element(By.ID,elmen.IDLogout).click()
        Urlogin = driver.current_url
        self.assertIn(Urlogin,Url.base_url)
        time.sleep(2)

    def tearDown(self):
        self.browser.quit()


if __name__ == "__main__":
    unittest.main()