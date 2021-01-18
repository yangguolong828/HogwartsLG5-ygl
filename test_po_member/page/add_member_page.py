from test_po_member.page.base_page import BasePage
from test_po_member.page.contact_page import ContactPage

class AddMemberaPage(BasePage):
    def add_member(self):
       return ContactPage()
