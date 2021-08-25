"""
Launch a browser and open google page. Search something on google and open the 3rd search result
"""
# INCORRECT
from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.google.com/")

# Open Google page, select search box and type "Selenium in it"
driver.find_element_by_xpath("//input[@title='Search']").send_keys("Selenium")

# Clicking on Google Search for Selenium
driver.find_element_by_xpath("(//input[@value='Google Search'])[1]").click()

# Select the search result which starts with "Selenium tutorials for beginners"
driver.find_element_by_xpath("//*[starts-with(text(),'Selenium Tutorial for Beginners')]").click()

time.sleep(2)

driver.quit()