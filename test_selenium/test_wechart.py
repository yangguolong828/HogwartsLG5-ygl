from selenium import webdriver
from selenium.webdriver.common.by import By


class TestWorlWechart():
    def setup(self):
        chrome_args = webdriver.ChromeOptions()
        chrome_args.debugger_address = "localhost:9222"
        self.driver = webdriver.Chrome(options=chrome_args)
    #
    # def teardown(self):
    #     self.driver.quit()

    def test_workwechart(self):
        self.driver.get("https://work.weixin.qq.com/")
        self.driver.find_element(By.XPATH, "//*[@class='index_top_operation_loginBtn']").click()