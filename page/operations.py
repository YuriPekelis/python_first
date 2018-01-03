class Operations:
    # def __init__(self):
        # self.driver = driver
    __INNER_HTML = "innerHTML"

    def click_element (self, element):
        element.click()

    def enter_text (self, element, text):
        element.send_keys(text)

    def clear_fld (self, element):
        element.clear()

    def fill_field_with_text (self, element, text):
        self.click_element(element)
        self.clear_fld(element)
        self.enter_text(element, text)

    def select_option_by_text (self, select, text):
        select.select_by_visible_text(text)



    def get_element_attribute (self, element, attr_name):
        return element.get_attribute(attr_name)

    def get_element_text (self, element):
        return self.get_element_attribute(element, self.__INNER_HTML)