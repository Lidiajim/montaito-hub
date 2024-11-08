# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestTestcreate():
    def setup_method(self, method):
        # Initialize ChromeDriver with explicit binary location
        options = webdriver.ChromeOptions()
        options.binary_location = "/usr/bin/google-chrome"
        
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        self.vars = {}
  
    def teardown_method(self, method):
        self.driver.quit()
  
    def test_testcreate(self):
        self.driver.get("http://127.0.0.1:5000/")
        self.driver.set_window_size(1050, 748)
        self.driver.find_element(By.LINK_TEXT, "Doe, John").click()
        self.driver.find_element(By.CSS_SELECTOR, ".dropdown-item:nth-child(2)").click()
        self.driver.find_element(By.ID, "email").click()
