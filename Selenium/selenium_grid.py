from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time

caps = DesiredCapabilities.FIREFOX

# caps['platform'] = "WINDOWS"
# caps['version'] = "10"

# caps['platform'] = "LINUX"
# caps['version'] = "16"

driver = webdriver.Remote("http://192.168.101.23:4444/wd/hub", caps)

driver.get("https://www.seleniumhq.org/")
time.sleep(5)
driver.quit()