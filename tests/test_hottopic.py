from page.page_hottopic import HotTopicPage
from tests.testrunner import TestRunner
from genie.genie import GenieExtension


class PythonOrgSearch(TestRunner):

    def test_hottopic(self):
        hot_topic_page = HotTopicPage(self.driver_wrapper, self.operations)
        hot_topic_page.get_homepage()
        hot_topic_page.search_product()
        hot_topic_page.select_product()
        hot_topic_page.add_product()
        hot_topic_page.get_to_cart()
        start_sum = hot_topic_page.get_total()
        genie = GenieExtension(self.driver_wrapper, self.operations)
        genie.apply_savings()
        final_sum = hot_topic_page.get_total()
        self.assertAlmostEqual(start_sum - genie.get_price_discount(), final_sum, delta=0.005)
        self.assertTrue(genie.is_close_btn_found() or genie.is_continue_btn_found())
        print(genie.get_result_message(start_sum, final_sum))
