from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ConfirmationPage:
    @staticmethod
    def waitForAlertBanner(driver):
        wait = WebDriverWait(driver, 10)
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "alert")))

    @staticmethod
    def getAlertBannerText(driver):
        return driver.find_element(By.CLASS_NAME, "alert").text
