import unittest
import sys
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

class AutTest(unittest.TestCase):

    def setUp(self):
        options = webdriver.FirefoxOptions()
        options.add_argument('--ignore-ssl-errors=yes')
        options.add_argument('--ignore-certificate-errors')
        server = "http://localhost:4444"

        self.browser = webdriver.Remote(command_executor=server, options=options)
        self.addCleanup(self.browser.quit)

    def test_homepage(self):
        if len(sys.argv) > 1:
            url = sys.argv[1]
        else:
            url = "http://docker-apache"

        # Ensure proper URL format
        if not url.startswith('http'):
            url = "http://" + url

        self.browser.get(url)
        self.browser.save_screenshot("screenshot.png")
        # Tidak ada assert, hanya mengambil screenshot

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], verbosity=2, warnings='ignore')