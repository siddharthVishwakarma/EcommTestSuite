import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from utils.config import Config

class TestSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get(Config.URL)
    
    def test_search(self):
        driver = self.driver
        driver.find_element(By.ID, "search-box").send_keys("Laptop")
        driver.find_element(By.ID, "search-button").click()
        self.assertIn("Search Results", driver.title)
    
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
