from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://formy-project.herokuapp.com/radiobutton")

button1 = driver.find_element("id", "radio-button-1") #found by ID
button2 = driver.find_element(By.CSS_SELECTOR, "input[value='option2']") # find by value
button3 = driver.find_element(By.XPATH, "/html/body/div/div[3]/input") #find by xpath

time.sleep(1)
button1.click()
time.sleep(1)
button2.click()
time.sleep(1)
button3.click()
time.sleep(1)
button1.click()
time.sleep(1)

driver.quit()


