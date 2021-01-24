from selenium.webdriver.common.by import By

from test_frame2.page.base_page import BasePage
from test_frame2.page.search_page import SearchPage


class MarketPage(BasePage):
    def goto_search(self):
        self.find_and_click((By.ID, "com.xueqiu.android:id/action_search"))
        return SearchPage(self.driver)