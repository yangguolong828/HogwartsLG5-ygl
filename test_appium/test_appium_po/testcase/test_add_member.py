from test_appium.test_appium_po.page.app import App


class TestAddMember:

    def setup(self):
        self.app = App()
        self.main = self.app.start().goto_main()

    def teardown(self):
        self.app.stop()

    def test_add_member(self):
        toast = self.main.goto_contact().goto_memberinvite().goto_add_member().\
            edit_name().edit_gender().edit_phonenum().click_save().get_toast()

        assert toast == "添加成功"