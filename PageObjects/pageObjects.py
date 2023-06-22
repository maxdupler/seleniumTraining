from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from FormPage import FormPage
from ConfirmationPage import ConfirmationPage
import unittest

class PageObjects(unittest.TestCase):
    def test_form_submission(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")  # Run in headless mode
        driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
        driver.get("https://formy-project.herokuapp.com/form")

        formPage = FormPage()
        formPage.submitForm(driver)

        confirmationPage = ConfirmationPage()
        confirmationPage.waitForAlertBanner(driver)

        alert_text = confirmationPage.getAlertBannerText(driver)
        expected_text = "The form was successfully submitted!"
        self.assertEqual(expected_text, alert_text)

        driver.quit()

# single test
#if __name__ == "__main__":
 #   unittest.main()

# multiple tests
if __name__ == "__main__":
    num_repeats = 10  # Number of times to repeat the test
    suite = unittest.TestSuite()
    for _ in range(num_repeats):
        suite.addTest(unittest.makeSuite(PageObjects))

    runner = unittest.TextTestRunner()
    result = runner.run(suite)