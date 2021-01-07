from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By


class TestHogwards():
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(3)

    def teardown(self):
        self.driver.quit()

    def test_hogwarts(self):
        self.driver.get("http://ceshiren.com/")
        self.driver.find_element(By.XPATH, '//*[@id="ember20"]/div/span').click()
        sleep(3)