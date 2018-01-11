from page.page_pizzahut import PizzaHutPage
from tests.testrunner import TestRunner
from genie.genie import GenieExtension


class PythonOrgSearch(TestRunner):


    def test_large_pizza(self):
        pizzahut_page = PizzaHutPage (self.driver_wrapper, self.operations)
        pizzahut_page.get_homepage()
        pizzahut_page.search_product()
        pizzahut_page.select_product()
        pizzahut_page.add_product()
        pizzahut_page.get_to_cart()
        start_sum = pizzahut_page.get_total()
        genie = GenieExtension(self.driver_wrapper, self.operations)
        genie.apply_savings()
        final_sum = pizzahut_page.get_total()
        self.assertAlmostEqual(start_sum - genie.get_price_discount(), final_sum, delta=0.005)
        self.assertTrue(genie.is_close_btn_found() or genie.is_continue_btn_found())
        print(genie.get_result_message(start_sum, final_sum))
