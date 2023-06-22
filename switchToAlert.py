from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://formy-project.herokuapp.com/switch-window")

openAlert = driver.find_element("id", "alert-button")

openAlert.click()

time.sleep(2)

alert = driver.switch_to.alert

alert.accept()

time.sleep(2)

driver.quit()

