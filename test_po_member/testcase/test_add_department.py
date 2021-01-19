
from test_po_member.page.contact_page import ContactPage



class TestAddDepartment():

    def setup_class(self):
        # 实例化contact类
        self.contact = ContactPage()

    def test_add_department(self):
        result= self.contact.goto_add_department().add_department().get_departmentlist()
        assert result == True
