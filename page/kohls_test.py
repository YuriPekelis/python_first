import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

from page.kohl_page import KohlPage
from page.text_utils import TextUtils
from .genie import GenieExtension
from .operations import Operations
from .difdata_kohls import DiffDataKohls
import os

class PythonOrgSearch(unittest.TestCase):
    GENIE_PATHNAME = "/home/ypeke/genie.crx"

    def setUp(self):
        # print(os.path.abspath(__file__))
        path = os.getcwd() + '/venv/chromedriver-Linux64'
        print(path)

        chrome_opt = Options()
        chrome_opt.add_extension(self.GENIE_PATHNAME)
        self.driver = webdriver.Chrome(chrome_options=chrome_opt)
        self.driver.implicitly_wait(10)

    def test_kohls(self):
        operations = Operations()
        kohl_page = KohlPage(self.driver, operations)
        kohl_page.get_homepage()
        kohl_page.search_product()
        kohl_page.slelect_product()
        kohl_page.add_product()
        kohl_page.get_to_cart()
        start_sum = kohl_page.get_total()
        genie = GenieExtension(self.driver, operations)
        genie.apply_savings()
        final_sum = kohl_page.get_total()
        self.assertEqual(start_sum - genie.get_price_discount(), final_sum)
        self.assertTrue (genie.is_close_btn_found() or genie.is_continue_btn_found())
        print(genie.get_result_message(start_sum, final_sum))

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
