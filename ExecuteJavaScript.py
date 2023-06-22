from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://formy-project.herokuapp.com/modal")

modalButton = driver.find_element("id", "modal-button")

modalButton.click()

time.sleep(1)

closeButton = driver.find_element("id", "close-button")

driver.execute_script("arguments[0].click();", closeButton)

time.sleep(1)

driver.quit()