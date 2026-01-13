import unittest
import sys
from selenium import webdriver
from selenium.webdriver.common.by import By

class AutTest(unittest.TestCase):

    def setUp(self):
        # Ambil browser dari argumen ke-2. Default ke 'firefox'
        browser_type = sys.argv[2] if len(sys.argv) > 2 else "firefox"
        
        # Logika pemilihan Options
        if browser_type == "chrome":
            options = webdriver.ChromeOptions()
        elif browser_type == "edge":
            options = webdriver.EdgeOptions()
        else:
            options = webdriver.FirefoxOptions()

        # Konfigurasi umum (SSL ignore)
        options.add_argument('--ignore-ssl-errors=yes')
        options.add_argument('--ignore-certificate-errors')
        
        server = 'http://localhost:4444'

        self.browser = webdriver.Remote(command_executor=server, options=options)
        self.addCleanup(self.browser.quit)

    def test_homepage(self):
        # Ambil URL dari argumen ke-1
        if len(sys.argv) > 1:
            url = sys.argv[1]
        else:
            url = "http://localhost"

        self.browser.get(url)
        expected_result = "Welcome back, Guest!"
        actual_result = self.browser.find_element(By.TAG_NAME, 'p')
        self.assertIn(expected_result, actual_result.text)

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], verbosity=2, warnings='ignore')