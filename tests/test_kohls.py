from page.page_kohl import KohlPage
from tests.testrunner import TestRunner
from genie.genie import GenieExtension


class PythonOrgSearch(TestRunner):

    def test_kohls(self):
        kohl_page = KohlPage(self.driver_wrapper, self.operations)
        kohl_page.get_homepage()
        kohl_page.search_product()
        kohl_page.select_product()
        kohl_page.add_product()
        kohl_page.get_to_cart()
        start_sum = kohl_page.get_total()
        genie = GenieExtension(self.driver_wrapper, self.operations)
        genie.apply_savings()
        final_sum = kohl_page.get_total()
        self.assertAlmostEqual(start_sum - genie.get_price_discount(), final_sum, delta=0.005)
        self.assertTrue(genie.is_close_btn_found() or genie.is_continue_btn_found())
        print(genie.get_result_message(start_sum, final_sum))
