# Launch a web browser and open a website. Take screenshot of that website

from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("https://www.youtube.com/")

# Take a screen shot of this webpage
driver.get_screenshot_as_file("youtube.png")

driver.quit()