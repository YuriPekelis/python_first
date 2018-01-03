import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from page.text_utils import TextUtils
from .genie import GenieExtension
from .operations import Operations
from .difdata_kohls import DiffDataKohls
import time


class PythonOrgSearch(unittest.TestCase):
    GENIE_PATHNAME = "c:/AutomationTools/genie.crx"

    def setUp(self):
        chrome_opt = Options()
        chrome_opt.add_extension(self.GENIE_PATHNAME)
        self.driver = webdriver.Chrome(chrome_options=chrome_opt)
        self.driver.implicitly_wait(30)
        self.operations = Operations()

    def test_large_pizza(self):
        driver = self.driver
        driver.get(DiffDataKohls.START_URL)
        operations = Operations()
        operations.fill_field_with_text(driver.find_element_by_id(DiffDataKohls.SEARCH_FIELD_ID),
                                        DiffDataKohls.PRODUCT_NAME)
        operations.enter_text(driver.find_element_by_id(DiffDataKohls.SEARCH_FIELD_ID),
                                        Keys.ENTER)
        # operations.click_element(driver.find_element_by_css_selector(DiffDataKohls.SIZE_BTN_CSS))
        operations.click_element(driver.find_elements_by_css_selector(DiffDataKohls.SIZE_BTNS_CSS)[0])
        operations.click_element(driver.find_element_by_id(DiffDataKohls.ADD_TO_BAG_BTN_ID))
        operations.click_element(driver.find_element_by_css_selector(DiffDataKohls.CHECKOUT_BTN_CSS))
        # operations.click_element(driver.find_element_by_id(DiffDataKohls.GUEST_CHECKOUT_BTN_ID))
        operations.click_element(driver.find_element_by_css_selector(DiffDataKohls.GUEST_CHECKOUT_BTN_ID))
        start_sum = TextUtils.extract_price_from_text(operations.get_element_text(
            driver.find_element_by_css_selector(DiffDataKohls.TOTAL_SUM_ID)))
        genie = GenieExtension(self.driver, self.operations)
        genie.apply_savings()
        final_sum = TextUtils.extract_price_from_text(operations.get_element_text(
            driver.find_element_by_css_selector(DiffDataKohls.TOTAL_SUM_ID)))
        self.assertEqual(start_sum - genie.get_price_discount(), final_sum)
        self.assertTrue(genie.is_close_btn_found() or genie.is_close_btn_found())
        print(genie.get_result_message(start_sum, final_sum))

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
