import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from utils.config import Config

class TestRegistration(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get(Config.URL)
    
    def test_registration(self):
        driver = self.driver
        driver.find_element(By.ID, "register-name").send_keys("Test User")
        driver.find_element(By.ID, "register-email").send_keys("testuser@example.com")
        driver.find_element(By.ID, "register-password").send_keys("password123")
        driver.find_element(By.ID, "register-button").click()
        self.assertIn("Welcome", driver.page_source)
    
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
