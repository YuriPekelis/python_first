from page.kohl_page import KohlPage
from page.testrunner import TestRunner
from .genie import GenieExtension
import os

class PythonOrgSearch(TestRunner):

    def test_kohls(self):
        # operations = Operations()
        kohl_page = KohlPage(self.driver, self.operations)
        kohl_page.get_homepage()
        kohl_page.search_product()
        kohl_page.slelect_product()
        kohl_page.add_product()
        kohl_page.get_to_cart()
        start_sum = kohl_page.get_total()
        genie = GenieExtension(self.driver, self.operations)
        genie.apply_savings()
        final_sum = kohl_page.get_total()
        self.assertEqual(start_sum - genie.get_price_discount(), final_sum)
        self.assertTrue (genie.is_close_btn_found() or genie.is_continue_btn_found())
        print(genie.get_result_message(start_sum, final_sum))

