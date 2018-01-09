from abc import ABC, abstractmethod


class BasePage(ABC):
    _driver_wrapper = None
    _operations = None

    def __init__(self, driver_wrapper, operations):
        self._driver_wrapper = driver_wrapper
        self._operations = operations

    @abstractmethod
    def get_homepage(self):
        pass

    @abstractmethod
    def search_product(self):
        pass

    @abstractmethod
    def select_product(self):
        pass

    @abstractmethod
    def add_product(self):
        pass

    @abstractmethod
    def get_to_cart(self):
        pass

    @abstractmethod
    def get_total(self):
        pass

    def _refresh_page (self):
        self._driver.refresh()
