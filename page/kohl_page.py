from selenium.webdriver.common.keys import Keys

from page.text_utils import TextUtils
from page.basepage import BasePage

class KohlPage (BasePage):


    __START_URL = "https://www.kohls.com/"
    __PRODUCT_NAME = "Cuddl Duds 6-Piece Red Plaid Flannel Comforter Set"
    __SEARCH_FIELD_CSS = "#search"
    __SIZE_BTN_CSS = ".pdp-product-size > .pdp-waist-size_info.clearfix > a:nth-child(1)"
    __SIZE_BTNS_CSS = ".pdp-product-size > .pdp-waist-size_info.clearfix > a"
    __ADD_TO_BAG_BTN_CSS = "#addtobagID"
    __VIEW_BAG_BTN_CSS = ".viewBag_ghr"
    __TOTAL_SUM_CSS = "#totalcharges"


    def add_product(self):
        """Add product to cart"""
        self._operations.click_element(self._driver.find_element_by_css_selector(self.__ADD_TO_BAG_BTN_CSS))

    def get_total(self):
        """:returns total sum of cart"""
        return TextUtils.extract_price_from_text(self._operations.get_element_text(
            self._driver.find_element_by_css_selector(self.__TOTAL_SUM_CSS)))

    def search_product(self):
        """Performs operations for search product"""
        self._operations.fill_field_with_text(self._driver.find_element_by_css_selector(self.__SEARCH_FIELD_CSS),
                                        self.__PRODUCT_NAME)
        self._operations.enter_text(self._driver.find_element_by_css_selector(self.__SEARCH_FIELD_CSS),
                              Keys.ENTER)

    def get_to_cart(self):
        """Performs operations for going to cart"""
        self._operations.click_element(self._driver.find_element_by_css_selector(self.__VIEW_BAG_BTN_CSS))


    def get_homepage(self):
        """Open home page"""
        self._driver.get(self.__START_URL)

    def slelect_product(self):
        """Performs operations for selecting a product"""
        self._operations.click_element(self._driver.find_element_by_css_selector(self.__SIZE_BTNS_CSS))
        #operations.click_element(driver.find_element_by_css_selector(DiffDataKohls.SIZE_BTN_CSS))
