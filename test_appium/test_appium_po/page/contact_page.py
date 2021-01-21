from appium.webdriver.common.mobileby import MobileBy

from test_appium.test_appium_po.page.base_page import BasePage
from test_appium.test_appium_po.page.memberInvite_page import MemberInvitePage


class ContactPage(BasePage):

    def goto_memberinvite(self):
        # self.find(MobileBy.ANDROID_UIAUTOMATOR,
        #           'new UiScrollable(new UiSelector().'
        #           'scrollable(true).instance(0)).'
        #           'scrollIntoView(new UiSelector().'
        #           'text("添加成员").instance(0));').click()
        self.scroll_find_click("添加成员")
        return MemberInvitePage(self.driver)