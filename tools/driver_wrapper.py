import time

from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium import webdriver
from selenium.webdriver import ChromeOptions, Proxy
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from tools.creds import Creds


class DriverWrapper:
    __driver = None

    def setup_simple_driver (self):
        chrome_opt = ChromeOptions()
        chrome_opt.add_extension(Creds.GENIE_PATHNAME)
        chrome_opt.add_argument("--start-maximized")
        self.__driver = webdriver.Chrome(chrome_options=chrome_opt)

    def setup_driver_proxy (self):
        chrome_opt = ChromeOptions()
        chrome_opt.add_extension(Creds.GENIE_PATHNAME)
        chrome_opt.add_argument("--start-maximized")
        proxy = Proxy({
            'proxyType': 'MANUAL',
            'httpProxy': Creds.PROXY,
            'ftpProxy': Creds.PROXY,
            'sslProxy': Creds.PROXY,
            'socksUsername':Creds.PROXY_USER,
            'socksPassword':Creds.PROXY_PASS,
            'class': "org.openqa.selenium.Proxy",
        })
        capabilities = dict(DesiredCapabilities.CHROME)
        capabilities['proxy'] = proxy

        proxy = {'address': Creds.PROXY,
                 'username': Creds.PROXY_USER,
                 'password': Creds.PROXY_PASS}

        capabilities = dict(DesiredCapabilities.CHROME)
        capabilities['proxy'] = {'proxyType': 'MANUAL',
                                 'httpProxy': proxy['address'],
                                 'ftpProxy': proxy['address'],
                                 'sslProxy': proxy['address'],
                                 'noProxy': '',
                                 'class': "org.openqa.selenium.Proxy",
                                 'autodetect': False}

        capabilities['proxy']['socksUsername'] = proxy['username']
        capabilities['proxy']['socksPassword'] = proxy['password']
        self.__driver = webdriver.Chrome(desired_capabilities = capabilities, chrome_options=chrome_opt)

    def open_page(self, url):
        """Open page on browser
        :param url : str - url address
        """
        self.__driver.get(url)

    def find_element_css(self, element_selector):
        """Finds an element by css selector
        :param element_selector: str - css selector of element
        :return WebElement - found WebElement
        """
        WebDriverWait(self.__driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, element_selector)))
        return self.__driver.find_element_by_css_selector(element_selector)

    def find_elements_css(self, elements_selector):
        """Finds elements by css selector
        :param elements_selector: str - css selector of elements
        :return array WebElements
        """
        return self.__driver.find_elements_by_css_selector(elements_selector)

    def is_element_presence_css(self, element_selector):
        """Checks presence of the element
        :param element_selector: str - css selector of element
        :return boolean - True if element is present, False if element is absent
        """
        WebDriverWait(self.__driver, 2).until(EC.presence_of_element_located((By.CSS_SELECTOR, element_selector)))
        return self.find_element_css(element_selector)

    def get_shadow_root_css(self, element_selector):
        """Finds using JS shadow root
        :param element_selector: str - css selector of the shadow root
        :return shadow root's WebElement
        """
        return self.__driver.execute_script('return arguments[0].shadowRoot', self.find_element_css(element_selector))

    def click_element_js_css(self, element_selector):
        """Clicks element using JS
        :param element_selector: str - css selector of the element
        """
        self.__driver.execute_script("$(arguments[0]).click();", self.find_element_css(element_selector))

    def wait(self, timeout):
        """Makes pause for the test
        :param timeout: float - time for test`s pause
        """
        time.sleep(timeout)

    def wait_element_css(self, element, timeout):
        """Explicity wait
        :param element: WenElement - an expecting element
        :param timeout: float - time for waiting process
        """
        WebDriverWait(self.__driver, timeout).until(EC._element_if_visible(element))

    def close(self):
        """Closes WebDiver """
        self.__driver.close()
