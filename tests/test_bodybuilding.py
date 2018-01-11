from tools.driver_wrapper import DriverWrapper
from tools.operations import Operations
from page.page_bodybuilding import BodyBuildingPage
from tests.testrunner import TestRunner
from genie.genie import GenieExtension


class PythonOrgSearch(TestRunner):

    def setUp(self):
        self.driver_wrapper = DriverWrapper()
        self.driver_wrapper.setup_driver_proxy()
        self.operations = Operations(self.driver_wrapper)

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
        self.assertAlmostEqual(start_sum - genie.get_price_discount(), final_sum, delta=0.005)
        self.assertTrue(genie.is_close_btn_found() or genie.is_continue_btn_found())
        print(genie.get_result_message(start_sum, final_sum))
