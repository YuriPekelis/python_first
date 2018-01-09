from page.bodybuilding_page import BodyBuildingPage
from page.testrunner import TestRunner
from .genie import GenieExtension


class PythonOrgSearch(TestRunner):

    def test_bodybuilding(self):
        bodybuilding_page = BodyBuildingPage(self.driver_wrapper, self.operations)
        bodybuilding_page.get_homepage()
        bodybuilding_page.search_product()
        bodybuilding_page.select_product()
        bodybuilding_page.add_product()
        bodybuilding_page.get_to_cart()
        start_sum = bodybuilding_page.get_total()
        genie = GenieExtension(self.driver_wrapper, self.operations)
        genie.apply_savings()
        final_sum = bodybuilding_page.get_total()
        self.assertEqual(start_sum - genie.get_price_discount(), final_sum)
        self.assertTrue(genie.is_close_btn_found() or genie.is_continue_btn_found())
        print(genie.get_result_message(start_sum, final_sum))