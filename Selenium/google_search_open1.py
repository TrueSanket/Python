"""
Launch a browser and open google page. Search something on google and open the "Books" link on tool bar
"""
#INCORRECT
from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.google.com/")

# Open Google page, select search box and type "Selenium in it"
driver.find_element_by_xpath("//input[@title='Search']").send_keys("Selenium")

# Clicking on Google Search for Selenium
driver.find_element_by_xpath("(//input[@value='Google Search'])[1]").click()

# Click on the "Books" link on tool bar

# Using Absolute Xpath method
driver.find_element_by_xpath("//*[@id='hdtb-msb']/div[1]/div/div[2]/a").click()

# Using tag name "Books" method (a =tag name, text function to search 'Books')
# driver.find_element_by_xpath("//a[text()='Books']").click()

time.sleep(2)

driver.quit()