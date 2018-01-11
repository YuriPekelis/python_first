from tools.text_utils import TextUtils
from page.basepage import BasePage


class KohlPage(BasePage):
    __START_URL = "https://www.kohls.com/"
    __PRODUCT_NAME = "Cuddl Duds 6-Piece Red Plaid Flannel Comforter Set"
    __SEARCH_FIELD_CSS = "#search"
    __SIZE_BTN_CSS = ".pdp-product-size > .pdp-waist-size_info.clearfix > a:nth-child(1)"
    __SIZE_BTNS_CSS = ".pdp-product-size > .pdp-waist-size_info.clearfix > a"
    __ADD_TO_BAG_BTN_CSS = "#addtobagID"
    __OPENED_BAG_BTN_CSS = ".mini-cart-header.loaded.loadedNewPB"
    __VIEW_BAG_BTN_CSS = ".viewBag_ghr"
    __TOTAL_SUM_CSS = "#totalcharges"

    def add_product(self):
        """Add product to cart"""
        self._operations.click_element_css(self.__ADD_TO_BAG_BTN_CSS)

    def get_total(self):
        """:returns total sum of cart"""
        return TextUtils.extract_price_from_text(self._operations.get_element_text_css(self.__TOTAL_SUM_CSS))

    def search_product(self):
        """Performs operations for search product"""
        self._operations.fill_field_with_text_and_press_enter(self.__SEARCH_FIELD_CSS, self.__PRODUCT_NAME)

    def get_to_cart(self):
        """Performs operations for going to cart"""
        if not self._driver_wrapper.is_element_presence_css(self.__VIEW_BAG_BTN_CSS):
            self._operations.click_element_css(self.__OPENED_BAG_BTN_CSS)
        self._operations.click_element_css(self.__VIEW_BAG_BTN_CSS)

    def get_homepage(self):
        """Open home page"""
        self._driver_wrapper.open_page(self.__START_URL)

    def select_product(self):
        """Performs operations for selecting a product"""
        self._operations.click_element_css(self.__SIZE_BTNS_CSS)
        # operations.click_element_css(driver.find_element_by_css_selector(DiffDataKohls.SIZE_BTN_CSS))
