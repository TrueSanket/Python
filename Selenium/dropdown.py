"""
Open a web browser and go to a website, find and print header of that web page then find a drop down menu on that
page and select item from that drop down menu and then shutdown the browser.
"""

from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://docs.python.org/3/")

time.sleep(2)

header = driver.find_element_by_xpath("//h1").text
print("Header is: ", header)

select = Select(driver.find_element_by_xpath("//select"))
time.sleep(2)
# Selecting item from drop down menu with three options: visible text, index number and value
# select.select_by_visible_text("French")
# select.select_by_index(2)       # In drop down menu, index number starts from 0
select.select_by_value("fr")

time.sleep(2)

driver.quit()