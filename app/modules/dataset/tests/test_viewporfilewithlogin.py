# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestViewporfilewithlogin():
  def setup_method(self, method):
    options = webdriver.ChromeOptions()
    self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_viewporfilewithlogin(self):
    self.driver.get("http://localhost:5000/login")
    self.driver.set_window_size(689, 696)
    self.driver.find_element(By.ID, "email").click()
    self.driver.find_element(By.ID, "email").send_keys("user1@example.com")
    self.driver.find_element(By.ID, "email").send_keys(Keys.ENTER)
    self.driver.find_element(By.ID, "password").click()
    self.driver.find_element(By.ID, "password").send_keys("1234")
    self.driver.find_element(By.ID, "password").send_keys(Keys.ENTER)
    self.driver.find_element(By.LINK_TEXT, "Sample dataset 4").click()
    self.driver.find_element(By.LINK_TEXT, "Doe, Jane").click()
    self.driver.get("http://localhost:5000")
    self.driver.find_element(By.LINK_TEXT, "Sample dataset 3").click()
    self.driver.find_element(By.LINK_TEXT, "Doe, John").click()
  
