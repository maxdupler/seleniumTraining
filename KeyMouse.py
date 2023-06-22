from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("https://formy-project.herokuapp.com/keypress")

name = driver.find_element("id", "name")
button = driver.find_element("id", "button")

name.send_keys("Max Dupler")
time.sleep(2)
button.click()

driver.quit()



