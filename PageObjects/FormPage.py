from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class FormPage:
    @staticmethod
    def submitForm(driver):
        driver.find_element(By.ID, "first-name").send_keys("John")
        driver.find_element(By.ID, "last-name").send_keys("Doe")
        driver.find_element(By.ID, "job-title").send_keys("QA Engineer")
        driver.find_element(By.ID, "radio-button-2").click()
        driver.find_element(By.ID, "checkbox-2").click()
        driver.find_element(By.CSS_SELECTOR, "option[value='1']").click()
        driver.find_element(By.ID, "datepicker").send_keys("05/28/2019")
        driver.find_element(By.ID, "datepicker").send_keys(Keys.RETURN)
        driver.find_element(By.CSS_SELECTOR, ".btn.btn-lg.btn-primary").click()
