import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from page.text_utils import TextUtils
from .genie import GenieExtension
from .operations import Operations
from .difdata_pizza import DiffDataPizza
import time


class PythonOrgSearch(unittest.TestCase):
    GENIE_PATHNAME = "c:/AutomationTools/genie.crx"

    def setUp(self):
        chrome_opt = Options()
        chrome_opt.add_extension(self.GENIE_PATHNAME)
        self.driver = webdriver.Chrome(chrome_options=chrome_opt)
        self.driver.implicitly_wait(10)
        self.operations = Operations()

    def test_large_pizza(self):
        driver = self.driver
        driver.get(DiffDataPizza.START_URL)
        operations = Operations()
        operations.click_element(driver.find_element_by_id(DiffDataPizza.MENU_BTN_ID))
        operations.click_element(driver.find_element_by_id(DiffDataPizza.PIZZA_SECTION_BTN_ID))
        operations.click_element(driver.find_element_by_xpath(DiffDataPizza.CHEESE_PIZZA_ORDER_NOW_BTN_XPATH))
        operations.click_element(driver.find_element_by_id(DiffDataPizza.CARRYOUT_BTN_ID))
        operations.fill_field_with_text(driver.find_element_by_css_selector(DiffDataPizza.ZIP_CODE_FLD_CSS),
                                        DiffDataPizza.ZIP_CODE)
        operations.click_element(driver.find_element_by_id(DiffDataPizza.FIND_A_STORE_BTN_ID))
        for current_location_block in driver.find_elements_by_css_selector(DiffDataPizza.LOCATIONS_BLOCKS_CSS):
            # location_number_element = current_location_block.find_element_by_css_selector(DiffData.LOCATION_NUMBER_IN_BLOCK_CSS)
            # location_number = location_number_element.get_attribute(DiffData.INNER_HTML)
            location_number = operations.get_element_text(
                current_location_block.find_element_by_css_selector(DiffDataPizza.LOCATION_NUMBER_IN_BLOCK_CSS))
            if (location_number == DiffDataPizza.NUMBER_ONE):
                # operations.click_element(current_location_block.find_element_by_class_name\
                #                              (DiffData.PRE_ORDER_BTN_INSIDE_BLOCK_CLS))
                operations.click_element(current_location_block.find_element_by_css_selector( \
                    DiffDataPizza.PRE_ORDER_BTN_INSIDE_BLOCK_CSS))
                break;
        WebDriverWait(driver, 10).until(
            (EC.visibility_of_element_located((By.ID, DiffDataPizza.CHEESE_PIZZA_SIZE_DROPDOWN_ID))))
        operations.select_option_by_text(
            Select(driver.find_element_by_id(DiffDataPizza.CHEESE_PIZZA_SIZE_DROPDOWN_ID)), \
            DiffDataPizza.LARGE)
        operations.click_element(driver.find_element_by_id(DiffDataPizza.ADD_TO_ORDER_BTN_ID))
        operations.click_element(driver.find_element_by_xpath(DiffDataPizza.CART_BTN_XPATH))
        start_sum = TextUtils.extract_price_from_text(operations.get_element_text(
            driver.find_element_by_css_selector(DiffDataPizza.SUBTOTAL_ORDER_SUM)))
        genie = GenieExtension(self.driver, self.operations)
        genie.apply_savings()
        final_sum = TextUtils.extract_price_from_text(operations.get_element_text(
            driver.find_element_by_css_selector(DiffDataPizza.SUBTOTAL_ORDER_SUM)))
        # print ("start sum {}".format(start_sum))
        # print ("discount {}".format(genie.get_price_discount()))
        # print ("final sum {}".format(final_sum))
        self.assertEqual(start_sum - genie.get_price_discount(), final_sum)
        self.assertTrue(genie.is_close_btn_found() or genie.is_close_btn_found())
        print(genie.get_result_message(start_sum, final_sum))

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
