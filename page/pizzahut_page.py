from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from page.text_utils import TextUtils
from page.basepage import BasePage

class PizzaHutPage (BasePage):

    __START_URL = "https://www.pizzahut.com/index.php#/menu/pizza/popular-pizzas"
    __MENU_BTN_CSS = "#lg-nav-menu"
    __PIZZA_SECTION_BTN_CSS = "#lg-nav-pizza"
    __CHEESE_PIZZA_ORDER_NOW_BTN_CSS = ".productButtons.ng-scope > a"
    __CARRYOUT_BTN_CSS = "#find-occasion-carryout"
    # ZIP_CODE_FLD_CSS = ".ng-valid-maxlength.ng-touched"
    __ZIP_CODE_FIELD_CSS = ".ph-padding-right-0 > input"
    __FIND_A_STORE_BTN_CSS = "#ph-find-store"
    # LOCATIONS_BLOCKS_CSS = ".row.ph-font-12.custom-ct-di.ng-scope"
    __ORDER_CARRYOUT_BTN_CSS = ".btn.ph-ordernow.ng-scope.btn-primary"
    # LOCATION_NUMBER_IN_BLOCK_CLS = "marker_label ng-binding"
    # LOCATION_NUMBER_IN_BLOCK_CSS = ".ng-binding"
    # PRE_ORDER_BTN_INSIDE_BLOCK_CLS = "btn ph-ordernow ng-scope btn-primary"
    # PRE_ORDER_BTN_INSIDE_BLOCK_CSS = ".btn.ph-ordernow.ng-scope.btn-primary"
    __CHEESE_PIZZA_SIZE_DROPDOWN_CSS = "#size-cheese-pizza"
    __ADD_TO_ORDER_BTN_CSS = "#ato-cheese-pizza"
    __CART_BTN_CSS = ".pointer-cursor > a.ph-ghost-link"
    __SUBTOTAL_ORDER_SUM_CSS = "#sub-total + .col-sm-6.text-right >.ng-binding"
    __TOTAL_ORDER_SUM_CSS = "div:not(#sub-total) + .col-sm-6.text-right > h4"
    __LARGE = "Large"
    __ZIP_CODE = "78701"


    def get_homepage(self):
        """Add product to cart"""
        self._driver.get(self.__START_URL)

    def search_product(self):
        self._operations.click_element(self._driver.find_element_by_css_selector(self.__MENU_BTN_CSS))
        self._operations.click_element(self._driver.find_element_by_css_selector(self.__PIZZA_SECTION_BTN_CSS))
        self._operations.click_element(self._driver.find_element_by_css_selector(self.__CHEESE_PIZZA_ORDER_NOW_BTN_CSS))
        self._operations.click_element(self._driver.find_element_by_css_selector(self.__CARRYOUT_BTN_CSS))
        self._operations.fill_field_with_text(self._driver.find_element_by_css_selector(self.__ZIP_CODE_FIELD_CSS),self.__ZIP_CODE)
        self._operations.click_element(self._driver.find_element_by_css_selector(self.__FIND_A_STORE_BTN_CSS))
        self._operations.click_element(self._driver.find_element_by_css_selector(self.__ORDER_CARRYOUT_BTN_CSS))
        
        # for current_location_block in self._driver.find_elements_by_css_selector(self.__LOCATIONS_BLOCKS_CSS):
        #     # location_number_element = current_location_block.find_element_by_css_selector(DiffData.LOCATION_NUMBER_IN_BLOCK_CSS)
        #     # location_number = location_number_element.get_attribute(DiffData.INNER_HTML)
        #     location_number = operations.get_element_text(
        #         current_location_block.find_element_by_css_selector(self.__LOCATION_NUMBER_IN_BLOCK_CSS))
        #     if (location_number == self.__NUMBER_ONE):
        #         # operations.click_element(current_location_block.find_element_by_class_name\
        #         #                              (DiffData.PRE_ORDER_BTN_INSIDE_BLOCK_CLS))
        #         operations.click_element(current_location_block.find_element_by_css_selector( \
        #             self.__PRE_ORDER_BTN_INSIDE_BLOCK_CSS))
        #         break;

    def slelect_product(self):
        WebDriverWait(self._driver, 2)
        self._operations.select_option_by_text(
            Select(self._driver.find_element_by_css_selector(self.__CHEESE_PIZZA_SIZE_DROPDOWN_CSS)), \
            self.__LARGE)
        
    def add_product(self):
        self._operations.click_element(self._driver.find_element_by_css_selector(self.__ADD_TO_ORDER_BTN_CSS))

    def get_to_cart(self):
        self._operations.click_element(self._driver.find_element_by_css_selector(self.__CART_BTN_CSS))

    def get_total(self):
        WebDriverWait(self._driver, 10).until(
            (EC.visibility_of_element_located((By.CSS_SELECTOR, self.__TOTAL_ORDER_SUM_CSS))))
        return TextUtils.extract_price_from_text(self._operations.get_element_text(
            self._driver.find_element_by_css_selector(self.__TOTAL_ORDER_SUM_CSS)))
        # return TextUtils.extract_price_from_text(self._operations.get_element_text(
        #     self._driver.find_element_by_css_selector(self.__SUBTOTAL_ORDER_SUM_CSS)))