import unittest, sys
from selenium import webdriver
from selenium.webdriver.common.by import By

class AutTest(unittest.TestCase):

    def setUp(self):
        browser = sys.argv[2] if len(sys.argv) > 2 else "firefox"

        if browser == "chrome":
            options = webdriver.ChromeOptions()
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-shm-usage")
        elif browser == "edge":
            options = webdriver.EdgeOptions()
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-shm-usage")
        else:
            options = webdriver.FirefoxOptions()

        options.add_argument("--headless")
        options.add_argument("--ignore-certificate-errors")

        self.browser = webdriver.Remote(
            command_executor="http://localhost:4444",
            options=options
        )
        self.addCleanup(self.browser.quit)


    def test_homepage(self):
        url = sys.argv[1] if len(sys.argv) > 1 else "http://localhost"

        self.browser.get(url)
        self.browser.save_screenshot("screenshot.png")
        expected_result = "Welcome back, Guest!"
        actual_result = self.browser.find_element(By.TAG_NAME, "p")

        self.assertIn(expected_result, actual_result.text)


if __name__ == "__main__":
    unittest.main(argv=["first-arg-is-ignored"], verbosity=2, warnings="ignore")