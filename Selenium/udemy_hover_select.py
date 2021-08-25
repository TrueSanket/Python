"""
Launch a web browser and open Udemy webpage. Select Categories >> IT & Software >> Network & Security >> Kubernetes.
After webpage loads, search for "Docker Mastery: with Kubernetes +Swarm from a Docker Captain" and select that course.
"""
#INCORRECT
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.udemy.com/")

wait = WebDriverWait(driver, 60)        # Waits until webpage completely loads

categories = driver.find_element_by_xpath("//span[contains(text(),'Categories')]")
hover = ActionChains(driver).move_to_element(categories)
hover.perform()

it_software = driver.find_element_by_xpath("(//div[contains(text(),'IT & Software')])[1]")
hover = ActionChains(driver).move_to_element(it_software)
hover.perform()

nw_security = driver.find_element_by_xpath("//div[contains(text(),'Network & Security')]")
hover = ActionChains(driver).move_to_element(nw_security)
hover.perform()

driver.find_element_by_xpath("//div[contains(text(),'Kubernetes')]").click()
time.sleep(2)

driver.find_element_by_xpath("(//div[starts-with(text(),'Docker Mastery')])[1]").click()

time.sleep(2)
driver.quit()