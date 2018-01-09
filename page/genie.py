from selenium.webdriver.support.wait import WebDriverWait

from .text_utils import TextUtils


class GenieExtension:
    __GOT_IT_BTN_CSS = ".dismiss-message"
    __GENIE_CONTAINER_CSS = "#__genie_container"
    __APPLY_SAVINGS_BTN = ".qa-test-codes"
    __CONTINUE_GENIE_BTN_CSS = ".qa-go-to-checkout"
    __CLOSE_GENIE_BTN_CSS_CSS = ".qa-close-results"
    __BUTTON_BLOCK_CSS = ".__rmnGenieResults--ctaWrapper"
    __COUPON_NAME_CSS = ".solvedCodeText"
    __DISCOUNT_PRICE_CSS = ".qa-codes-amount"
    __coupon_name = ""
    __price_discount = 0.00
    __is_continue_btn_found = False
    __is_close_btn_found = False
    __operations = None
    __driver_wrapper = None

    def __init__(self, driver_wrapper, operations):
        """ :param driver: Webdriver
            :param operations instance for work with WebElements
            """
        self.__driver_wrapper = driver_wrapper
        self.__operations = operations

    def __get_shadow_root(self):
        """:returns shadow_root of extension"""
        return self.__driver_wrapper.get_shadow_root_css(self.__GENIE_CONTAINER_CSS)

    def __get_shadow_root_element_css (self, element_selector):
        return self.__get_shadow_root().find_element_by_css_selector(element_selector)

    def __get_apply_savings_btn(self):
        """:returns returns Apply Savings button WebElement"""
        return self.__get_shadow_root_element_css(self.__APPLY_SAVINGS_BTN)

    def __get_continue_btn(self):
        """:returns returns Continue button WebElement"""
        return self.__get_shadow_root_element_css(self.__CONTINUE_GENIE_BTN_CSS)

    def __get_close_btn(self):
        """:returns returns Close button WebElement"""
        return self.__get_shadow_root_element_css(self.__CLOSE_GENIE_BTN_CSS_CSS)

    def __get_coupon_name_element(self):
        """:returns returns element that consist found coupon name"""
        return self.__get_shadow_root_element_css(self.__COUPON_NAME_CSS)

    def __get_coupon_name_text(self):
        """:returns returns found coupon name"""
        return self.__operations.get_element_text(self.__get_coupon_name_element())

    def __get_price_discount_element(self):
        """:returns returns element that consist discount sum text"""
        return self.__get_shadow_root_element_css(self.__DISCOUNT_PRICE_CSS)

    def __get_price_discount_text(self):
        """:returns returns discount sum text"""
        return self.__operations.get_element_text(self.__get_price_discount_element())

    def __is_shadow_element_present_css (self, element_selector):
        return self.__get_shadow_root().find_elements_by_css_selector(element_selector)

    def apply_savings(self):
        """Performs coupon`s search process"""
        self.__operations.click_element(self.__get_apply_savings_btn())
        counter = 0
        while counter < 60 and not self.__is_shadow_element_present_css(self.__BUTTON_BLOCK_CSS):
            self.__driver_wrapper.wait(1)
            counter += 1
            print(counter)
        result_btn = None
        if self.__is_shadow_element_present_css(self.__CONTINUE_GENIE_BTN_CSS):
            result_btn = self.__get_continue_btn()
            self.__price_discount = TextUtils.extract_price_from_text(self.__get_price_discount_text())
            self.__coupon_name = self.__get_coupon_name_text()
            self.__is_continue_btn_found = True
        elif self.__is_shadow_element_present_css(self.__CLOSE_GENIE_BTN_CSS_CSS):
            result_btn = self.__get_close_btn()
            self.__is_close_btn_found = True
        self.__operations.click_element(result_btn)

    def is_continue_btn_found(self):
        """:returns true if coupon has been found and search process was finished"""
        return self.__is_continue_btn_found

    def is_close_btn_found(self):
        """:returns true if coupon hasn't been found and search process was finished"""
        return self.__is_close_btn_found

    def get_price_discount(self):
        """:returns price discount, if a coupon has not been found then 0.0"""
        return self.__price_discount

    def get_coupon_name(self):
        """:returns found coupon's name"""
        return self.__coupon_name

    def get_result_message(self, start_sum, final_sum):
        """:returns message about result"""
        result = None
        if self.__is_continue_btn_found:
            result = "The Coupon {} was found. Start sum = {}, discount= {}, final sum = {}" \
                .format(self.get_coupon_name(), start_sum, self.__price_discount, final_sum)
        elif self.__is_close_btn_found:
            result = "Coupons were not found. Start sum = {}, discount= {}, final sum = {}" \
                .format(start_sum, self.__price_discount, final_sum)
        return result
