import time
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement


class Operations:
    __INNER_HTML = "innerHTML"
    __driver_wrapper = None

    def __init__(self, driver_wrapper):
        self.__driver_wrapper = driver_wrapper

    def click_element(self, element):
        """Click element
        :param element: WebElement - element
        """
        element.click()

    def click_element_css(self, element_selector):
        """Click element
        :param element_selector: str - css selector of element
        """
        self.__driver_wrapper.find_element_css(element_selector).click()

    def click_element_css_optional(self, element_selector):
        """Tries to click an element
        :param element_selector: str - css selector of element
        """
        try:
            self.click_element_css(element_selector)
        except Exception:
            pass

    def is_element_clickable_css(self, element_selector):
        """Checks if element is clickable
        :param element_selector: str - css selector of element
        :return boolean - True for clickable, false for unclickable
        """
        found_elements = self.__driver_wrapper.find_elements_css(element_selector)
        return found_elements and found_elements[0].is_displayed()

    def click_element_if_clickable_css(self, element_selector):
        """Click element if it is clickable
        :param element_selector: str - css selector of element
        :return boolean - True if an element was clicked, false if an element was not clicked
        """
        result = False
        if self.is_element_clickable_css(element_selector):
            self.click_element_css(element_selector)
            result = True
        return result

    def enter_text_css(self, element_selector, text):
        """Enters text to a field
        :param element_selector: str - css selector of field
        :param text: str - text for input
        """
        self.__driver_wrapper.find_element_css(element_selector).send_keys(text)

    def clear_fld(self, element_selector):
        """Clears a field
        :param element_selector: str - css selector of field
        """
        self.__driver_wrapper.find_element_css(element_selector).clear()

    def fill_field_with_text(self, element_selector, text):
        """Fill a field with text
        :param element_selector: str - css selector of field
        :param text: str - text for input
        """
        self.clear_fld(element_selector)
        self.enter_text_css(element_selector, text)

    def fill_field_with_text_and_press_enter(self, element_selector, text):
        """Fill a field with text and presses Enter button
        :param element_selector: str - css selector of field
        :param text: str - text for input
        """
        self.fill_field_with_text(element_selector, text)
        self.enter_text_css(element_selector, Keys.ENTER)

    def get_select_by_css(self, element_selector):
        """Finds Select element
        :param element_selector: str - css selector of Select element
        :return Select - Select element
        """
        return Select(self.__driver_wrapper.find_element_css(element_selector))

    def select_option_css_by_text(self, element_selector, text):
        """Makes choice for Select element by visible text
        :param element_selector: str - css selector of Select element
        :param text: str - visible text for choosing
        """
        self.get_select_by_css(element_selector).select_by_visible_text(text)

    def select_by_css_last_option(self, element_selector):
        """Makes choice of the last option for Select element
        :param element_selector: str - css selector of Select element
        """
        select = self.get_select_by_css(element_selector)
        select.select_by_index(len(select.options) - 1)

    def get_element_attribute_css(self, element_selector, attr_name):
        """Gets attribute from WebElement
        :param element_selector: str - css selector of element
        :param attr_name: str - name of the attribute
        :return WebElement`s attribute
        """
        return self.__driver_wrapper.find_element_css(element_selector).get_attribute(attr_name)

    def get_element_text_css(self, element_selector):
        """Gets text from WebElement
        :param element_selector: str - css selector of element
        :return WebElement`s text
        """
        return self.get_element_attribute_css(element_selector, self.__INNER_HTML)

    def get_element_attribute(self, element, attr_name):
        """Gets attribute from WebElement
        :param element: WebElement - WebElement
        :param attr_name: str - name of the attribute
        :return WebElement`s attribute
        """
        return element.get_attribute(attr_name)

    def get_element_text(self, element):
        """Gets text from WebElement
        :param element: WebElement - WebElement
        :return WebElement`s text
        """
        return self.get_element_attribute(element, self.__INNER_HTML)
