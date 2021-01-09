from time import sleep

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains


class TestActionChains():
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_case_click(self):
       element_click = self.driver.find_element(By.XPATH, '//*[@value="click me"]')
       element_doubleclick = self.driver.find_element_by_xpath('//input[@value="dbl click me"]')
       element_rightclick = self.driver.find_element_by_xpath('//input[@value="right click me"]')
       action = ActionChains(self.driver)
       action.click(element_click)
       action.double_click(element_doubleclick)
       action.context_click(element_rightclick)
       sleep(3)
       action.perform()
       sleep(3)

if __name__ == '__main__':
    pytest.main(['-v','-s','test_ActionChains.py'])