from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://formy-project.herokuapp.com/dropdown")

dropButton = driver.find_element("id", "dropdownMenuButton")
dropButton.click()
time.sleep(1)

autocomplete = driver.find_element("id", "autocomplete")
autocomplete.click()
time.sleep(1)

driver.quit()
