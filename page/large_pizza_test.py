import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from page.pizzahut_page import PizzaHutPage
from page.text_utils import TextUtils
from .genie import GenieExtension
from .operations import Operations
from .difdata_pizza import DiffDataPizza
import time


class PythonOrgSearch(unittest.TestCase):
    GENIE_PATHNAME = "/home/ypeke/genie.crx"

    def setUp(self):
        chrome_opt = Options()
        chrome_opt.add_extension(self.GENIE_PATHNAME)
        self.driver = webdriver.Chrome(chrome_options=chrome_opt)
        self.driver.implicitly_wait(10)
        self.operations = Operations()

    def test_large_pizza(self):
        operations = Operations()
        pizzahut_page = PizzaHutPage (self.driver, operations)
        pizzahut_page.get_homepage()
        pizzahut_page.search_product()
        pizzahut_page.slelect_product()
        pizzahut_page.add_product()
        pizzahut_page.get_to_cart()
        start_sum = pizzahut_page.get_total()
        genie = GenieExtension(self.driver, self.operations)
        genie.apply_savings()
        final_sum = pizzahut_page.get_total()
        print (start_sum)
        print(genie.get_price_discount())
        print(final_sum)
        self.assertEqual(start_sum - genie.get_price_discount(), final_sum)
        self.assertTrue(genie.is_close_btn_found() or genie.is_continue_btn_found())
        print(genie.get_result_message(start_sum, final_sum))

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
