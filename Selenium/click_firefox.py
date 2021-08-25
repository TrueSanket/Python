# Open a web site on firefox web browser and click on few sections and close the browser

from selenium import webdriver
import time

driver = webdriver.Firefox()
driver.maximize_window()     # maximize the web browser window
driver.get("https://www.selenium.dev/")

# Click on the sections of that website and hold for 2 seconds on that page
driver.find_element_by_link_text("Downloads").click()
time.sleep(2)

driver.find_element_by_link_text("Documentation").click()
time.sleep(2)

driver.find_element_by_link_text("Projects").click()
time.sleep(2)

driver.find_element_by_link_text("Support").click()
time.sleep(2)

# driver.close()  # Closes the current tab of that browser

driver.quit()  # closes all the tabs of the browser