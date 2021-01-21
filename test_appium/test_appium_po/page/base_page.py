from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:



    def find(self, by, value):
        return self.driver.find_element(by=by, value=value)

    def __init__(self, driver: WebDriver = None):
        self.driver = driver

    def find_and_click(self, para):
        self.find(para).click()

    def scroll_find_click(self, text):
        ele = self.find(MobileBy.ANDROID_UIAUTOMATOR,
                  'new UiScrollable(new UiSelector().'
                  'scrollable(true).instance(0)).'
                  'scrollIntoView(new UiSelector().'
                  f'text("{text}").instance(0));')
        self.find_and_click(ele)

    def find_and_get_text(self, para):
        self.find(para).text