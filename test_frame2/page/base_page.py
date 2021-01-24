from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:


    def __init__(self, driver: WebDriver = None):
        self.driver = driver

    def find_by(self, by, value):
        return self.driver.find_element(by=by,value=value)

    def find(self, locator):
        black_list = (By.XPATH, '//*[@id="com.xueqiu.android:id/iv_close"]')
        try:
            result = self.driver.find_element(*locator)
            return result
        except Exception as e:
            for black in black_list:
                eles = self.driver.find_element(*black)
                if len(eles)>0:
                    eles[0].click()

                    return self.find(locator)
            raise e


    def find_and_click(self, locator):
        self.find(locator).click()

    def find_and_send(self, locator):
        self.find(locator).send_keys()

    def scroll_find_click(self, text):
        ele = (MobileBy.ANDROID_UIAUTOMATOR,
                  'new UiScrollable(new UiSelector().'
                  'scrollable(true).instance(0)).'
                  'scrollIntoView(new UiSelector().'
                  f'text("{text}").instance(0));')
        self.find_and_click(ele)

    def find_and_get_text(self, locator):
        return self.find(locator).text