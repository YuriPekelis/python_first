import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from .operations import Operations
from .difdata import DiffData
import time


class PythonOrgSearch(unittest.TestCase):
    GENIE_PATHNAME = "c:/AutomationTools/genie.crx"
    EXPECTED_RESULT = 7.99

    def setUp(self):
        chrome_opt = Options()
        chrome_opt.add_extension(self.GENIE_PATHNAME)
        self.driver = webdriver.Chrome(chrome_options=chrome_opt)
        self.driver.implicitly_wait(10)
        self.operations = Operations()

    def test_large_pizza(self):
        driver = self.driver
        driver.get("https://www.pizzahut.com/index.php#/menu/pizza/popular-pizzas")
        operations = Operations()
        operations.click_element(driver.find_element_by_id(DiffData.MENU_BTN_ID))
        operations.click_element(driver.find_element_by_id(DiffData.PIZZA_SECTION_BTN_ID))
        operations.click_element(driver.find_element_by_xpath(DiffData.CHEESE_PIZZA_ORDER_NOW_BTN_XPATH))
        operations.click_element(driver.find_element_by_id(DiffData.CARRYOUT_BTN_ID))
        operations.input_fld(driver.find_element_by_css_selector(DiffData.ZIP_CODE_FLD_CSS), DiffData.ZIP_CODE)
        operations.click_element(driver.find_element_by_id(DiffData.FIND_A_STORE_BTN_ID))
        for current_location_block in driver.find_elements_by_css_selector(DiffData.LOCATIONS_BLOCKS_CSS):
            # location_number_element = current_location_block.find_element_by_css_selector(DiffData.LOCATION_NUMBER_IN_BLOCK_CSS)
            # location_number = location_number_element.get_attribute(DiffData.INNER_HTML)
            location_number = current_location_block.find_element_by_css_selector(DiffData.LOCATION_NUMBER_IN_BLOCK_CSS) \
                .get_attribute(DiffData.INNER_HTML)
            if (location_number == DiffData.NUMBER_ONE):
                # operations.click_element(current_location_block.find_element_by_class_name\
                #                              (DiffData.PRE_ORDER_BTN_INSIDE_BLOCK_CLS))
                operations.click_element(current_location_block.find_element_by_css_selector( \
                    DiffData.PRE_ORDER_BTN_INSIDE_BLOCK_CSS))
                break;
        WebDriverWait(driver, 10).until(
            (EC.visibility_of_element_located((By.ID, DiffData.CHEESE_PIZZA_SIZE_DROPDOWN_ID))))
        operations.select_option_by_text(Select(driver.find_element_by_id(DiffData.CHEESE_PIZZA_SIZE_DROPDOWN_ID)), \
                                         DiffData.LARGE)
        operations.click_element(driver.find_element_by_id(DiffData.ADD_TO_ORDER_BTN_ID))
        operations.click_element(driver.find_element_by_xpath(DiffData.CART_BTN_XPATH))
        shadow_root = driver.execute_script('return arguments[0].shadowRoot', \
                                            driver.find_element_by_id(DiffData.GENIE_CONTAINER_ID))
        operations.click_element(shadow_root.find_element_by_css_selector(DiffData.APPLY_SAVINGS_BTN))
        operations.click_element(shadow_root.find_element_by_css_selector(DiffData.CONTINUE_GENIE_BTN_CSS))
        actual_result = driver.find_element_by_css_selector("#sub-total + .col-sm-6.text-right >.ng-binding").get_attribute('innerHTML')
        actual_result = actual_result.replace("$", "")
        print(actual_result)
        actual_result_price = float(actual_result)
        self.assertEqual(self.EXPECTED_RESULT, actual_result_price)

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
