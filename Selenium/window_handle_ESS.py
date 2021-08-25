"""
Open a web browser and print it's window parent ID, if another window pops up then print it's child ID. Locate login
window and fill information and after that locate password window and fill password and hit enter.
"""
# INCORRECT

from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://ess.gslab.com/essgslab/")   # Website not opening up
time.sleep(2)
"""
# Get parent window id before opening new window
window_before = driver.window_handles[0]
print("window id parent-"+window_before)
driver.find_element_by_id("Image2").click()

# Get child window id after opening new window
window_after = driver.window_handles[1]
print("window id child-"+window_after)
time.sleep(2)

# By default focus will be on parent window, you need to switch to child window
driver.switch_to.window(window_after)

# Locate user name text box, clear text box contents & enter data
username = driver.find_element_by_id("txtUserName")
username.clear()
username.send_keys("abc@gslab.com")

# Locate password text box, clear text box contents & enter data
password = driver.find_element_by_id("txtPassword")
password.clear()
password.send_keys("password")

# click on login button
login_button = driver.find_element_by_id("btnLogin")
login_button. click()
"""

# quit will close all windows, opened by current driver session
driver.quit()
