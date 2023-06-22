from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://formy-project.herokuapp.com/scroll")

name = driver.find_element("id", "name")
date = driver.find_element("id", "date")

actions = ActionChains(driver)
actions.move_to_element(name)
name.send_keys("Max Dupler")
date.send_keys("02/04/2003")

time.sleep(4)


driver.quit()
