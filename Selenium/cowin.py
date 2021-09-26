"""
Launch a browser and open Cowin website. Sign in into the account and filter to 18-44 age, hospitals in Thane district
and Covishield doses and search for open slots after 5th September.
"""

import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome()
driver.maximize_window()
time.sleep(1)
driver.get("https://www.cowin.gov.in/")
wait = WebDriverWait(driver, 60)
time.sleep(2)

driver.find_element_by_xpath("//a[@title='Register / Sign In']").click()

driver.switch_to.window(driver.window_handles[1])
time.sleep(5)

driver.find_element_by_xpath("//input[@id='mat-input-0']").send_keys("9321620754")
driver.find_element_by_xpath("//ion-button[contains(text(),'Get OTP')]").click()
time.sleep(2)

time.sleep(30)

verifyproceed = driver.find_element_by_xpath("//ion-button[contains(text(),'Verify & Proceed')]")
driver.execute_script("arguments[0].scrollIntoView();", verifyproceed)
time.sleep(1)
driver.find_element_by_xpath("//ion-button[contains(text(),'Verify & Proceed')]").click()

schedule = driver.find_element_by_xpath("//span[contains(text(),'Schedule')]")
driver.execute_script("arguments[0].scrollIntoView();", schedule)
time.sleep(1)
driver.find_element_by_xpath("//span[contains(text(),'Schedule')]").click()
time.sleep(2)
driver.find_element_by_xpath("//button[@data-checked='Search By District']").click()
time.sleep(2)

state = Select(driver.find_element_by_xpath("//div[@id='mat-select-value-1']"))
time.sleep(1)
state.select_by_visible_text("Maharashtra")
time.sleep(1)
district = Select(driver.find_element_by_xpath("//mat-select[@id='mat-select-6']"))
time.sleep(1)
district.select_by_visible_text("Thane")
time.sleep(1)

search = driver.find_element_by_xpath("//ion-button[contains(text(),'Search')]")
driver.execute_script("arguments[0].scrollIntoView();", search)
time.sleep(1)
driver.find_element_by_xpath("//ion-button[contains(text(),'Search')]").click()
time.sleep(2)

driver.quit()