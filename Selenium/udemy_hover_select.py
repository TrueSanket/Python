"""
Launch a web browser and open Udemy webpage. Select Categories >> IT & Software >> Network & Security >> Kubernetes.
After webpage loads, search for "Docker Mastery: with Kubernetes +Swarm from a Docker Captain" and select that course.
"""

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.udemy.com/")

wait = WebDriverWait(driver, 60)        # Waits until webpage completely loads
time.sleep(3)

categories = driver.find_element_by_xpath("//span[contains(text(),'Categories')]")
hover = ActionChains(driver).move_to_element(categories)
hover.perform()
time.sleep(1)

it_software = driver.find_element_by_xpath("(//div[contains(text(),'IT & Software')])[1]")
hover = ActionChains(driver).move_to_element(it_software)
hover.perform()
time.sleep(1)

nw_security = driver.find_element_by_xpath("//div[contains(text(),'Network & Security')]")
hover = ActionChains(driver).move_to_element(nw_security)
hover.perform()
time.sleep(1)

driver.find_element_by_xpath("//div[contains(text(),'Kubernetes')]").click()
time.sleep(2)

k8s = driver.find_element_by_xpath("//img[@src='https://img-c.udemycdn.com/course/240x135/1035000_c1aa_6.jpg']")
driver.execute_script("arguments[0].scrollIntoView();", k8s)
time.sleep(1)

driver.find_element_by_xpath("(//div[starts-with(text(),'Docker Mastery')])[1]").click()
time.sleep(2)

print("Found the Kubernetes course!")
driver.quit()