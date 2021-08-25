from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://www.seleniumhq.org")
driver.implicitly_wait(10)

driver.find_element_by_xpath("//span[contains(text(),'Documentation')]").click()
time.sleep(5)

# Navigate a page back
driver.back()
time.sleep(5)

# Navigate a page forward
driver.forward()
time.sleep(5)

# Refresh the page
driver.refresh()
time.sleep(5)

driver.quit()