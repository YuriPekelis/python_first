from .base_page import BasePage

class KohlPage (BasePage):

    __START_URL = "https://www.kohls.com/"
    __PRODUCT_NAME = "Cuddl Duds 6-Piece Red Plaid Flannel Comforter Set"
    __SEARCH_FIELD_ID = "search"
    __SIZE_BTN_CSS = ".pdp-product-size > .pdp-waist-size_info.clearfix > a:nth-child(1)"
    __SIZE_BTNS_CSS = ".pdp-product-size > .pdp-waist-size_info.clearfix > a"
    __ADD_TO_BAG_BTN_ID = "addtobagID"
    __CHECKOUT_BTN_CSS = ".checkout-link"#"#checkout-container > a:nth-child(1)"
    __GUEST_CHECKOUT_BTN_ID = "LPGuestCheckout"
    __TOTAL_SUM_ID = "totalcharges"

    def add_product(self):
        pass

    def get_total(self):
        pass

    def search_product(self):
        pass

    def get_to_cart(self):
        pass

    def get_homepage(self):
        self._driver.get

    def slelect_product(self):
        pass