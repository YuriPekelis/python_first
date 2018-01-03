from abc import ABC, abstractmethod


class BasePage(ABC):
    _driver = None
    _operations = None

    def __init__(self, driver, operations):
        self._driver = driver
        self._operations = operations

    @abstractmethod
    def get_homepage(self):
        pass

    @abstractmethod
    def search_product(self):
        pass

    @abstractmethod
    def slelect_product(self):
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
