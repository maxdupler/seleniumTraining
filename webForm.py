import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class FormTest(unittest.TestCase):

    def setUp(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")  # Run in headless mode
        self.driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
        self.driver.get("https://formy-project.herokuapp.com/form")

    def tearDown(self):
        self.driver.quit()

    def test_form_submission(self):
        firstName = self.driver.find_element("id", "first-name")
        lastName = self.driver.find_element("id", "last-name")
        jobTitle = self.driver.find_element("id", "job-title")
        radioButton2 = self.driver.find_element("id", "radio-button-2")
        checkbox1 = self.driver.find_element("id", "checkbox-1")
        menu = self.driver.find_element(By.CSS_SELECTOR, "option[value='1']")
        datePicker = self.driver.find_element("id", "datepicker")
        submit = self.driver.find_element(By.CSS_SELECTOR, ".btn.btn-lg.btn-primary")

        firstName.send_keys("Max")
        lastName.send_keys("Dupler")
        jobTitle.send_keys("QA Intern")
        radioButton2.click()
        checkbox1.click()
        menu.click()
        datePicker.send_keys("06/22/2023")
        datePicker.send_keys(Keys.RETURN)  # close datepicker
        #time.sleep(4)
        submit.click()
        #time.sleep(1)

        # Explicit wait
        wait = WebDriverWait(self.driver, 10)  # wait for a max of 10s
        alert = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "alert")))

        alert_text = alert.text
        expected_text = "The form was successfully submitted!"
        self.assertEqual(expected_text, alert_text)

#if __name__ == "__main__":   #single test
    #unittest.main()

# multiple tests
if __name__ == "__main__":
    num_repeats = 10  # Number of times to repeat the test
    suite = unittest.TestSuite()
    for _ in range(num_repeats):
        suite.addTest(unittest.makeSuite(FormTest))

    runner = unittest.TextTestRunner()
    result = runner.run(suite)