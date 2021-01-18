        # 设置页面等待
# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy


class TestDemo:
    def setup(self):
        caps = {}
        caps["platformName"] = "android"
        caps["deviceName"] = "127.0.0.1:7555"
        caps["appPackage"] = "com.tencent.wework"
        caps["appActivity"] = ".launch.LaunchSplashActivity"
        # 不清空本地缓存，启动app
        caps["noReset"] = "true"
        caps["ensureWebviewsHavePages"] = True
        # 设置页面等待空闲时间为0秒
        caps['settings[waitForIdleTimeout]']  = 0


        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)

        self.driver.implicitly_wait(10)

    def teardown(self):
        self.driver.quit()

    def test_demo(self):

        el1 = self.driver.find_element_by_id("com.tencent.wework:id/ie_")
        el1.click()
        el2 = self.driver.find_element_by_id("com.tencent.wework:id/gwt")
        el2.send_keys("寻喃")
        el3 = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.RelativeLayout[2]/android.widget.RelativeLayout/android.widget.RelativeLayout[1]/android.widget.RelativeLayout")
        el3.click()
        el4 = self.driver.find_element_by_id("com.tencent.wework:id/etm")
        el4.send_keys("111")
        el5 = self.driver.find_element_by_id("com.tencent.wework:id/eti")
        el5.click()

    def test_daka(self):
        self.driver.find_element(MobileBy.XPATH, "//*[@text='工作台']").click()
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                 'new UiScrollable(new UiSelector().'
                                 'scrollable(true).instance(0)).'
                                 'scrollIntoView(new UiSelector().'
                                 'text("打卡").instance(0));').click()
        self.driver.find_element(MobileBy.XPATH,"//*[@text='外出打卡']").click()
        self.driver.find_element(MobileBy.XPATH,"//*[contains(@text,'次外出')]").click()
        result = self.driver.find_element(MobileBy.ID,"com.tencent.wework:id/pt").text
        assert result == "外出打卡成功"

