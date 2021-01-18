import json
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By


class BasePage():

    def __init__(self, base_driver=None):
        # base_driver:webdriver
        if base_driver is None:
            self.driver = webdriver.Chrome()
            self.driver.maximize_window()
            self._cookie_login()
            self.driver.implicitly_wait(3)
        else:
            self.driver = base_driver


    def _cookie_login(self):
        self.driver.get("https://work.weixin.qq.com/")
        #以文件流的形式打开文件
        with open("../testcase/cookie.json", "r") as f:
            #读取cookie
            cookies = json.load(f)
        #注入cookie
        for cookie in cookies:
            self.driver.add_cookie(cookie)
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        sleep(3)
        self.driver.find_element(By.XPATH, '//*[@id="menu_contacts"]').click()