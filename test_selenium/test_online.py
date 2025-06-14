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

class TestOnline():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_online(self):
    self.driver.get("http://127.0.0.1:56988/")
    self.driver.set_window_size(1306, 792)
    self.driver.find_element(By.CSS_SELECTOR, ".col-md-4:nth-child(2) .hot-product-card-img-overlay").click()
    self.driver.find_element(By.CSS_SELECTOR, ".cymbal-button-primary").click()
    self.driver.find_element(By.LINK_TEXT, "Continue Shopping").click()
    self.driver.find_element(By.CSS_SELECTOR, ".col-md-4:nth-child(3) .hot-product-card-img-overlay").click()
    self.driver.find_element(By.CSS_SELECTOR, ".cymbal-button-primary").click()
    self.driver.find_element(By.CSS_SELECTOR, ".cymbal-button-secondary").click()
    self.driver.find_element(By.CSS_SELECTOR, ".col-md-4:nth-child(4) .hot-product-card-img-overlay").click()
    self.driver.find_element(By.CSS_SELECTOR, ".cymbal-button-primary").click()
    self.driver.find_element(By.CSS_SELECTOR, ".cymbal-button-primary:nth-child(1)").click()
    self.driver.find_element(By.LINK_TEXT, "Continue Shopping").click()
  
