from tools.text_utils import TextUtils
from page.basepage import BasePage


class BodyBuildingPage(BasePage):
    __START_URL = "https://www.bodybuilding.com/index.html"
    __PRODUCT_NAME = "ISO100, 5 Lbs."
    __NECESSARY_TOTAL = 300.00
    __SEARCH_FIELD_CSS = ".typeahead__search-field"
    __PRODUCT_NAME_LINK_CSS = ".product__mobile-click-target"
    __VIEW_PRODUCT_BTN_CSS = ".product__view-product-link"
    __IMAGE_PRODUCT_LINK_CSS = ".product__img-wrapper"
    __PRODUCT_GROUP_CSS = ".SkuGroup"
    __PRODUCT_GROUP_PRICE_CSS = ".SkuGroup__sale-price"
    __ORDER_BTNS_CSS = ".SkuGroup__sku__order__btn"
    __KEEP_SHOPPING_BTN_CSS = ".add2cart__checkout__stay"
    __VIEW_BAG_BTN_CSS = ".add2cart__checkout__view-cart"

    __QUANTITY_SELECT_CSS = ".quantity-select > select"
    __SUBTOTAL_SUM_CSS = "#floating-checkout-repel-target > div > .order-subtotal__price"

    def add_product(self):
        """Add product to cart"""
        if self._operations.click_element_if_clickable_css(self.__PRODUCT_NAME_LINK_CSS):
            pass
        elif self._operations.click_element_if_clickable_css(self.__VIEW_PRODUCT_BTN_CSS):
            pass
        elif self._operations.click_element_if_clickable_css(self.__IMAGE_PRODUCT_LINK_CSS):
            pass
        max_price = 0.0
        max_price_product_group = None
        for current_product_group in self._driver_wrapper.find_elements_css(self.__PRODUCT_GROUP_CSS):
            current_product_group_price = TextUtils.extract_price_from_text(
                self._operations.get_element_text(
                    current_product_group.find_element_by_css_selector(self.__PRODUCT_GROUP_PRICE_CSS)))
            if current_product_group_price > max_price:
                max_price = current_product_group_price
                max_price_product_group = current_product_group
        self._operations.click_element(max_price_product_group.find_element_by_css_selector(self.__ORDER_BTNS_CSS))

    def get_total(self):
        """:returns total sum of cart"""
        return TextUtils.extract_price_from_text(self._operations.get_element_text_css(self.__SUBTOTAL_SUM_CSS))

    def search_product(self):
        """Performs operations for search product"""
        self._operations.fill_field_with_text_and_press_enter(self.__SEARCH_FIELD_CSS, self.__PRODUCT_NAME)

    def get_to_cart(self):
        """Performs operations for going to cart"""
        self._operations.click_element_css(self.__VIEW_BAG_BTN_CSS)
        self._operations.select_by_css_last_option(self.__QUANTITY_SELECT_CSS)

    def get_homepage(self):
        """Open home page"""
        self._driver_wrapper.open_page(self.__START_URL)

    def select_product(self):
        pass
