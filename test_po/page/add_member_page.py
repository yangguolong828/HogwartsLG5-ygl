from test_po.page.base_page import BasePage
from test_po.page.contact_page import ContactPage

class AddMemberaPage(BasePage):
    def add_member(self):
       return ContactPage()
