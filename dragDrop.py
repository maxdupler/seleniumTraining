from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://formy-project.herokuapp.com/dragdrop")

image = driver.find_element("id", "image")
dropBox = driver.find_element("id", "box")

time.sleep(1)

actions = ActionChains(driver)

actions.drag_and_drop(image, dropBox).perform()

time.sleep(2)

driver.quit()


