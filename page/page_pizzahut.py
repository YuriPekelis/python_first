import time

from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait

from page.text_utils import TextUtils
from page.basepage import BasePage


class PizzaHutPage(BasePage):
    __START_URL = "https://www.pizzahut.com"
    __MENU_BTN_CSS = ".dropdown-toggle"
    __PIZZA_SECTION_BTN_CSS = ".dropdown-item"
    __CHEESE_PIZZA_ORDER_NOW_BTN_CSS = ".productButtons.ng-scope > a"
    __CARRYOUT_BTN_CSS = "#find-occasion-carryout"
    __ZIP_CODE_FIELD_CSS = ".ph-padding-right-0 > input"
    __FIND_A_STORE_BTN_CSS = "#ph-find-store"
    __ORDER_CARRYOUT_BTN_CSS = ".btn.ph-ordernow.ng-scope.btn-primary"
    __CHEESE_PIZZA_SIZE_DROPDOWN_CSS = "#size-cheese-pizza"
    __ADD_TO_ORDER_BTN_CSS = "#ato-cheese-pizza"
    __CART_BTN_CSS = ".pointer-cursor > a.ph-ghost-link"
    __SUBTOTAL_ORDER_SUM_CSS = "#sub-total + .col-sm-6.text-right >.ng-binding"
    __TOTAL_ORDER_SUM_CSS = "div:not(#sub-total) + .col-sm-6.text-right > h4"
    __LARGE = "Large"
    __ZIP_CODE = "78701"

    def get_homepage(self):
        """Open home page"""
        self._driver_wrapper.open_page(self.__START_URL)

    def search_product(self):
        """Performs operations for choosing product"""
        self._operations.click_element_css(self.__MENU_BTN_CSS)
        self._operations.click_element_css(self.__PIZZA_SECTION_BTN_CSS)
        self._operations.click_element_css(self.__CHEESE_PIZZA_ORDER_NOW_BTN_CSS)
        self._operations.click_element_css(self.__CARRYOUT_BTN_CSS)
        self._operations.fill_field_with_text(self.__ZIP_CODE_FIELD_CSS, self.__ZIP_CODE)
        self._operations.click_element_css(self.__ZIP_CODE_FIELD_CSS)
        self._operations.click_element_css(self.__FIND_A_STORE_BTN_CSS)
        self._operations.click_element_css(self.__ORDER_CARRYOUT_BTN_CSS)

    def select_product(self):
        """Performs operations for selecting product's parameters"""
        self._operations.select_option_css_by_text(self.__CHEESE_PIZZA_SIZE_DROPDOWN_CSS, self.__LARGE)

    def add_product(self):
        """Add product to cart"""
        self._operations.click_element_css(self.__ADD_TO_ORDER_BTN_CSS)

    def get_to_cart(self):
        """Performs operations for going to cart"""
        self._operations.click_element_css(self.__CART_BTN_CSS)

    def get_total(self):
        """:returns total sum of cart"""
        time.sleep(2)
        return TextUtils.extract_price_from_text(self._operations.get_element_text_css(self.__TOTAL_ORDER_SUM_CSS))
