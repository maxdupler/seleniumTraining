from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://formy-project.herokuapp.com/datepicker")

dateField = driver.find_element("id", "datepicker")

dateField.send_keys("02/04/2025")
time.sleep(1)
dateField.send_keys(Keys.RETURN)
time.sleep(1)

driver.quit()