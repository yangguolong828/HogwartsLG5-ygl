from test_po.page.base_page import BasePage
from test_po.page.main_page import MainPage


class TestAddMember(BasePage):

    def setup_class(self):
        pass

    def test_add_member(self):

        main = MainPage()

        result = main.goto_add_member().add_member().get_list()