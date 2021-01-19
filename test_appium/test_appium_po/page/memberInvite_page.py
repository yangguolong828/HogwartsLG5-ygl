from appium.webdriver.common.mobileby import MobileBy

from test_appium.test_appium_po.page.add_member_page import AddMemberPage
from test_appium.test_appium_po.page.base_page import BasePage

# 点击手动添加
class MemberInvitePage(BasePage):

    def goto_add_member(self):
        self.find(MobileBy.XPATH, '//*[@text="手动输入添加"]').click()
        return AddMemberPage(self.driver)

    def get_toast(self):
        result = self.find(MobileBy.XPATH, '//*[@class="android.widget.Toast"]').text
        return result