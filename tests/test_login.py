import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from utils.config import Config

class TestLogin(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get(Config.URL)
    
    def test_login(self):
        driver = self.driver
        driver.find_element(By.ID, "login-username").send_keys(Config.USERNAME)
        driver.find_element(By.ID, "login-password").send_keys(Config.PASSWORD)
        driver.find_element(By.ID, "login-button").click()
        self.assertIn("Dashboard", driver.title)
    
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
