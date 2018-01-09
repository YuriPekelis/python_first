from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

from page.text_utils import TextUtils
from page.basepage import BasePage


class HotTopicPage(BasePage):
    __START_URL = "https://www.hottopic.com"
    __CLOSE_EMAIL_INPUT_BTN_CSS = ".ui-dialog-titlebar-close"
    __PRODUCT_NAME = "Pokemon Pikachu Face Flip Crossbody Bag"
    __SEARCH_FIELD_CSS = "#q"
    __QTY_DROPDOWN_CSS = "#Quantity"
    __ADD_TO_CART_CSS = "#add-to-cart"
    __GO_TO_SHOPPING_BAG_CSS = ".mini-cart-link"
    __KEEP_SHOPPING_BTN_CSS = ".add2cart__checkout__stay"
    __VIEW_BAG_BTN_CSS = ".MiniCart__link"
    __TOTAL_SUM_CSS = ".orderTotal"
    __AAA = ".ui-dialog.ui-widget"

    def add_product(self):
        """Add product to cart"""
        self._operations.click_element_css(self.__ADD_TO_CART_CSS)

    def get_total(self):
        """:returns total sum of cart"""
        return TextUtils.extract_price_from_text(self._operations.get_element_text_css(self.__TOTAL_SUM_CSS))

    def search_product(self):
        """Performs operations for search product"""
        self._operations.fill_field_with_text_and_press_enter(self.__SEARCH_FIELD_CSS, self.__PRODUCT_NAME)

    def get_to_cart(self):
        """Performs operations for going to cart"""
        self._operations.click_element_css(self.__GO_TO_SHOPPING_BAG_CSS)

    def get_homepage(self):
        """Open home page"""
        self._driver_wrapper.open_page(self.__START_URL)
        self._driver_wrapper.click_element_js_css(self.__CLOSE_EMAIL_INPUT_BTN_CSS)

    def select_product(self):
        """Performs operations for selecting a product"""
        self._operations.select_by_css_last_option(self.__QTY_DROPDOWN_CSS)
