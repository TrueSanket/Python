import time
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.python.org/accounts/login/")

wait = WebDriverWait(driver, 60)        # Waits until webpage completely loads

driver.find_element_by_xpath("//input[@id='id_login']").send_keys("admin")
time.sleep(2)

driver.find_element_by_xpath("//input[@id='id_password']").send_keys("admin123")
time.sleep(2)

element = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='id_remember']")))
element.click()

header = driver.find_element_by_xpath("//h1[contains(text(),'Sign In')]").text
print("Title of the page: ", header)

time.sleep(2)

driver.quit()