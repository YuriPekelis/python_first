from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from . import operations
from .text_utils import TextUtils


class GenieExtension:
    __GENIE_CONTAINER_ID = "__genie_container"
    __APPLY_SAVINGS_BTN = ".rmnGenie-button.qa-test-codes"
    __CONTINUE_GENIE_BTN_CSS = ".qa-go-to-checkout.rmnGenie-button"
    __CLOSE_GENIE_BTN_CSS_CSS = ".qa-close-results.rmnGenie-button"
    __BUTTON_BLOCK_CSS = ".__rmnGenieResults--ctaWrapper"
    __DISCOUNT_PRICE_CSS = "rmnGenie-bigText rmnGenie-boldText rmnGenie-whiteText qa-codes-amount"
    __shadow_root = None
    __price_discount = 0.00
    __is_continue_btn_found = False
    __is_close_btn_found = False
    __operations = None
    __driver = None

    def __init__(self, driver, operations):
        self.__driver = driver
        self.__operations = operations
        self.__shadow_root = self.__get_shadow_root()

    def __get_shadow_root (self):
        return self.__driver.execute_script('return arguments[0].shadowRoot', \
                                                   self.__driver.find_element_by_id(self.__GENIE_CONTAINER_ID))

    def __get_apply_savings_btn(self):
        return self.__get_shadow_root().find_element_by_css_selector(self.__APPLY_SAVINGS_BTN)

    def __get_continue_btn(self):
        return self.__get_shadow_root().find_element_by_css_selector(self.__CONTINUE_GENIE_BTN_CSS)

    def __get_close_btn(self):
        return self.__get_shadow_root().find_element_by_css_selector(self.__CLOSE_GENIE_BTN_CSS_CSS)

    def __get_price_discount_element(self):
        return self.__get_shadow_root().find_element_by_css_selector(self.__DISCOUNT_PRICE_CSS)

    def __get_price_discount_text(self):
        return self.__operations.get_element_text(self.__get_price_discount_element())

    def apply_savings(self):
        self.__operations.click_element(self.__get_apply_savings_btn())
        counter = 0
        while (counter < 60 or len(self.__shadow_root.find_elements_by_css_selector(self.__BUTTON_BLOCK_CSS)) == 0):
            WebDriverWait(self.__driver, 1)
            counter += 1
        result_btn = None
        if (len(self.__get_shadow_root().find_elements_by_css_selector(self.__CONTINUE_GENIE_BTN_CSS)) > 0):
            result_btn = self.__get_continue_btn()
            self.__price_discount = TextUtils.extract_price_from_text(self.__get_price_discount_text())
            operations.click_element(self.__get_continue_btn())
            self.__is_continue_btn_found = True
        if (len(self.__get_shadow_root().find_elements_by_css_selector(self.__CLOSE_GENIE_BTN_CSS_CSS)) > 0):
            result_btn = self.__get_close_btn()
            self.__is_close_btn_found = True
        self.__operations.click_element(result_btn)

    def is_continue_btn_found(self):
        return self.__is_continue_btn_found

    def is_close_btn_found(self):
        return self.__is_close_btn_found

    def get_price_discount(self):
        return self.__price_discount

    def get_result_message(self, start_sum, final_sum):
        result = None
        if (self.__is_continue_btn_found):
            result = "The Coupon was found. Start sum :{}, discount: {}, final sum {}" \
                .format(start_sum, self.__price_discount, final_sum)
        if (self.__is_close_btn_found):
            result = "The Coupon was not found. Sum hasn`t been changed: {}".format(start_sum)
        return result
