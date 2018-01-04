import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from page.operations import Operations


class TestRunner (unittest.TestCase):

    GENIE_PATHNAME = "/home/ypeke/genie.crx"

    def setUp(self):
        chrome_opt = Options()
        chrome_opt.add_extension(self.GENIE_PATHNAME)
        self.driver = webdriver.Chrome(chrome_options=chrome_opt)
        self.driver.implicitly_wait(10)
        self.operations = Operations()

    def tearDown(self):
        self.driver.close()

    if __name__ == "__main__":
        unittest.main()