import unittest

from selenium import webdriver
from selenium.webdriver import Proxy
# from selenium.webdriver.chrome.options import Options
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.proxy import ProxyType

from page.operations import Operations
from page.driver_wrapper import DriverWrapper
from .creds import Creds


class TestRunner(unittest.TestCase):




    # GENIE_PATHNAME = "/home/ypeke/genie.crx"

    def setUp(self):

        # # 1 option - uncomment and add constant`s values for BodyBuilder
        # proxy = Proxy({
        #     'proxyType': 'MANUAL',
        #     'httpProxy': Creds.PROXY,
        #     'ftpProxy': Creds.PROXY,
        #     'sslProxy': Creds.PROXY,
        #     'socksUsername':Creds.PROXY_USER,
        #     'socksPassword':Creds.PROXY_PASS,
        #     'class': "org.openqa.selenium.Proxy",
        # })
        # # proxy.proxy_type(ProxyType.MANUAL)
        # # proxy.httpProxy(Creds.PROXY)
        # # proxy.socks_username(Creds.PROXY_USER)
        # # proxy.socks_password(Creds.PROXY_PASSWORD)
        # chrome_opt = ChromeOptions()
        # chrome_opt.add_extension(Creds.GENIE_PATHNAME)
        # chrome_opt.add_argument("--start-maximized")
        #
        # capabilities = dict(DesiredCapabilities.CHROME)
        # proxy.add_to_capabilities(capabilities)
        # driver = webdriver.Chrome(desired_capabilities = capabilities, chrome_options=chrome_opt)


        ### 2 option - uncomment and add constant`s values for BodyBuilder
        # chrome_opt = ChromeOptions()
        # chrome_opt.add_extension(Creds.GENIE_PATHNAME)
        # chrome_opt.add_argument("--start-maximized")
        # proxy = Proxy({
        #     'proxyType': 'MANUAL',
        #     'httpProxy': Creds.PROXY,
        #     'ftpProxy': Creds.PROXY,
        #     'sslProxy': Creds.PROXY,
        #     'socksUsername':Creds.PROXY_USER,
        #     'socksPassword':Creds.PROXY_PASS,
        #     'class': "org.openqa.selenium.Proxy",
        # })
        # capabilities = dict(DesiredCapabilities.CHROME)
        # capabilities['proxy'] = proxy
        #
        # proxy = {'address': Creds.PROXY,
        #          'username': Creds.PROXY_USER,
        #          'password': Creds.PROXY_PASS}
        #
        # capabilities = dict(DesiredCapabilities.CHROME)
        # capabilities['proxy'] = {'proxyType': 'MANUAL',
        #                          'httpProxy': proxy['address'],
        #                          'ftpProxy': proxy['address'],
        #                          'sslProxy': proxy['address'],
        #                          'noProxy': '',
        #                          'class': "org.openqa.selenium.Proxy",
        #                          'autodetect': False}
        #
        # capabilities['proxy']['socksUsername'] = proxy['username']
        # capabilities['proxy']['socksPassword'] = proxy['password']
        # driver = webdriver.Chrome(desired_capabilities = capabilities, chrome_options=chrome_opt)

        ### 3 option - regular webdriver for all tests except bodybuilder
        chrome_opt = ChromeOptions()
        chrome_opt.add_extension(Creds.GENIE_PATHNAME)
        chrome_opt.add_argument("--start-maximized")
        driver = webdriver.Chrome(chrome_options=chrome_opt)





        self.driver_wrapper = DriverWrapper (driver)
        self.operations = Operations(self.driver_wrapper)

    def tearDown(self):
        self.driver_wrapper.close()

    if __name__ == "__main__":
        unittest.main()
