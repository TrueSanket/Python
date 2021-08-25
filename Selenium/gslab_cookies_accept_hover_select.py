"""
Launch GS Lab website on chrome and accept cookies. Now, Hover over an element in the menu and select another element
from that hover drop down.
"""

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.webdriver.support.ui import WebDriverWait


driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://www.gslab.com/')

wait = WebDriverWait(driver, 60)        # Waits until webpage completely loads

driver.find_element_by_id("hs-eu-confirmation-button").click()
time.sleep(2)

technology_solutions = driver.find_element_by_link_text("Technology Solutions")
hover = ActionChains(driver).move_to_element(technology_solutions)
hover.perform()

driver.find_element_by_link_text("Telecom").click()
time.sleep(2)

driver.quit()