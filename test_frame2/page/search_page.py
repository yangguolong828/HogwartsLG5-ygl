from selenium.webdriver.common.by import By

from test_frame2.page.base_page import BasePage


class SearchPage(BasePage):
    def search(self):
        self.find_by(By.ID, "com.xueqiu.android:id/search_input_text").send_keys("阿里巴巴")
        self.find_and_click((By.XPATH, '//*[@text="阿里巴巴-SW"]'))
