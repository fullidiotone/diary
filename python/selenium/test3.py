from pyvirtualdisplay import Display
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest

class GoogleTestCase(unittest.TestCase):

    def setUp(self):
        self.display = Display(visible=0, size=(800, 600))
        self.display.start()
        self.browser = webdriver.Chrome()
        self.addCleanup(self.browser.quit)

    def testPageTitle(self):
        self.browser.get('http://www.google.com')
        self.assertIn('ZZZZe', self.browser.title)

if __name__ == '__main__':
    unittest.main(verbosity=2)
