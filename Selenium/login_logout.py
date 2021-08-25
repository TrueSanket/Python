# Login to an account of a webpage and logout successfully

import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
# Use different website
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.netmanias.com/en/")

wait = WebDriverWait(driver, 60)   # Waits until webpage completely loads

driver.find_element_by_xpath("//a[contains(text(),'Login')]").click()
time.sleep(2)

driver.find_element_by_xpath("//input[@name='user_id']").send_keys("sanketjkulkarni")
time.sleep(2)

driver.find_element_by_xpath("//input[@name='user_pwd']").send_keys("Januaryz@7")
time.sleep(2)

driver.find_element_by_xpath("(//div[contains(text(),'Login')])[3]").click()
time.sleep(5)

driver.find_element_by_xpath("//a[contains(text(),'Logout')]").click()

time.sleep(5)
driver.quit()