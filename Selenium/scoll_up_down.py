# Open a web page and scroll up and down and then close the browser

import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome()
driver.maximize_window()
time.sleep(1)
driver.get("https://www.countries-ofthe-world.com/flags-of-the-world.html")

wait = WebDriverWait(driver, 60)
time.sleep(2)

# Scroll down the page by pixel
"""
driver.execute_script("window.scrollBy(0,1000)","")
time.sleep(1)
"""
# Scroll down the page till we find required element
"""
flag = driver.find_element_by_xpath("//td[contains(text(),'India')]")
driver.execute_script("arguments[0].scrollIntoView();", flag)
time.sleep(2)
"""
# Scroll to the end of the page
"""
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
time.sleep(1)
"""
driver.quit()