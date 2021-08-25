import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

# Launch chrome browser and open sauce lab webpage

driver = webdriver.Chrome()
driver.maximize_window()
time.sleep(1)
driver.get("https://www.saucedemo.com/")

wait = WebDriverWait(driver, 60)
time.sleep(2)

# Login into the account with given credentials

driver.find_element_by_xpath("//input[@id='user-name']").send_keys("standard_user")
time.sleep(1)
driver.find_element_by_xpath("//input[@id='password']").send_keys("secret_sauce")
time.sleep(1)
driver.find_element_by_xpath("//input[@id='login-button']").click()
time.sleep(3)

# Add any two items to the cart from available items and go to cart

driver.find_element_by_xpath("//button[@id='add-to-cart-sauce-labs-backpack']").click()
time.sleep(2)
driver.find_element_by_xpath("//button[@id='add-to-cart-sauce-labs-fleece-jacket']").click()
time.sleep(2)
driver.find_element_by_xpath("//a[@class='shopping_cart_link']").click()
time.sleep(3)
driver.find_element_by_xpath("//button[@id='checkout']").click()
time.sleep(2)

# Checkout with name and zip code

driver.find_element_by_xpath("//input[@id='first-name']").send_keys("Tyrion")
time.sleep(1)
driver.find_element_by_xpath("//input[@id='last-name']").send_keys("Lannister")
time.sleep(1)
driver.find_element_by_xpath("//input[@id='postal-code']").send_keys("77095")
time.sleep(2)
driver.find_element_by_xpath("//input[@id='continue']").click()
time.sleep(2)

# Proceed to final page, scroll down, submit order and print thank you page

finish = driver.find_element_by_xpath("//button[@id='finish']")
driver.execute_script("arguments[0].scrollIntoView();", finish)
time.sleep(1)
driver.find_element_by_xpath("//button[@id='finish']").click()
time.sleep(2)
success = driver.find_element_by_xpath("//h2").text
print(success)

#  Log out successfully and close browser

driver.find_element_by_xpath("//button[@id='react-burger-menu-btn']").click()
time.sleep(1)
driver.find_element_by_xpath("//a[@id='logout_sidebar_link']").click()
time.sleep(2)

driver.quit()