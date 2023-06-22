from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://formy-project.herokuapp.com/switch-window")

newTab = driver.find_element("id", "new-tab-button")

newTab.click()

originalHandle = driver.current_window_handle

time.sleep(2)

for handle in driver.window_handles:
    driver.switch_to.window(handle)

time.sleep(2)

driver.switch_to.window(originalHandle)

time.sleep(2)

driver.quit()

