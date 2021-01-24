from selenium.webdriver.common.by import By

from test_appium.test_frame_serchpage.base_page import BasePage
from test_appium.test_frame_serchpage.page.markert_page import MarketPage


class MainPage(BasePage):
    def goto_market_page(self):
        self.find((By.ID, "com.xueqiu.android:id/post_status"))
        self.find_and_click((By.XPATH, '//*[@text="行情"]'))
        return MarketPage(self.driver)