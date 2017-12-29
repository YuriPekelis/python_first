class Operations:
    # def __init__(self):
        # self.driver = driver

    def click_element (self, element):
        element.click()

    def input_fld (self, element, text):
        self.click_element(element)
        self.clear_fld(element)
        element.send_keys (text)

    def select_option_by_text (self, select, text):
        select.select_by_visible_text(text)

    def clear_fld (self, element):
        element.clear()