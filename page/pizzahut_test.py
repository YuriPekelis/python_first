from page.pizzahut_page import PizzaHutPage
from page.testrunner import TestRunner
from .genie import GenieExtension


class PythonOrgSearch(TestRunner):


    def test_large_pizza(self):
        pizzahut_page = PizzaHutPage (self.driver, self.operations)
        pizzahut_page.get_homepage()
        pizzahut_page.search_product()
        pizzahut_page.slelect_product()
        pizzahut_page.add_product()
        pizzahut_page.get_to_cart()
        start_sum = pizzahut_page.get_total()
        genie = GenieExtension(self.driver, self.operations)
        genie.apply_savings()
        final_sum = pizzahut_page.get_total()
        print (start_sum)
        print(genie.get_price_discount())
        print(final_sum)
        self.assertEqual(start_sum - genie.get_price_discount(), final_sum)
        self.assertTrue(genie.is_close_btn_found() or genie.is_continue_btn_found())
        print(genie.get_result_message(start_sum, final_sum))
