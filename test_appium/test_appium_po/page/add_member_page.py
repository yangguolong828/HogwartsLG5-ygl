from appium.webdriver.common.mobileby import MobileBy

from test_appium.test_appium_po.page.base_page import BasePage


# 编辑成员的信息
class AddMemberPage(BasePage):

    def edit_name(self):
        self.find(MobileBy.XPATH, '//*[contains(@text,"姓名")]/../android.widget.EditText').send_keys("张三1")
        return self
    def edit_gender(self):
        gender = '男'
        self.find(MobileBy.XPATH, '//*[@text="男"]').click()
        if gender == '女':
            self.find(MobileBy.XPATH, '//*[@text="女"]').click()
        else:
            self.find(MobileBy.XPATH, '//*[@resource-id="com.tencent.wework:id/boh"]//*[@text="男"]').click()
        return self
    def edit_phonenum(self):
        self.find(MobileBy.ID, "com.tencent.wework:id/fuy").send_keys("13212312341")
        return self
    def click_save(self):
        from test_appium.test_appium_po.page.memberInvite_page import MemberInvitePage
        self.find(MobileBy.ID, "com.tencent.wework:id/ie7").click()
        return MemberInvitePage(self.driver)