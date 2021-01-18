from test_po_department.page.base_page import BasePage


class NewContactPage(BasePage):
    def teardown(self):
        self.driver.quit()

    def goto_adddepartment(self):
        pass

    def add_department(self):
        pass

    def add_member(self):
        pass

    def get_memberlist(self):
        pass

    def get_departmentlist(self):
        """
        返回通讯录页面的组织架构信息
        :retrun:
        """
        return True

