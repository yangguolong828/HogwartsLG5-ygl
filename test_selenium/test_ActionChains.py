from time import sleep

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

from test_selenium.base import Base


class TestActionChains(Base):

    @pytest.mark.skip
    def test_case_click(self):
        self.driver.get("http://sahitest.com/demo/clicks.htm")
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

    @pytest.mark.skip
    def test_movetoelement(self):
        self.driver.get("http://www.baidu.com")
        self.driver.maximize_window()
        ele = self.driver.find_element(By.XPATH, '//*[@id="s-usersetting-top"]')
        action = ActionChains(self.driver)
        action.move_to_element(ele)
        action.perform()
        sleep(3)

    @pytest.mark.skip
    def test_dragdrop(self):
        self.driver.get("http://sahitest.com/demo/dragDropMooTools.htm")
        self.driver.maximize_window()
        ele_drag = self.driver.find_element_by_id("dragger")
        ele_drop = self.driver.find_element_by_xpath("/html/body/div[2]")

        action = ActionChains(self.driver)
        # action.drag_and_drop(ele_drag,ele_drop).perform()
        action.click_and_hold(ele_drag).move_to_element(ele_drop).release().perform()
        sleep(3)

    def test_keys(self):
        self.driver.get("http://sahitest.com/demo/label.htm")
        ele_user = self.driver.find_element_by_xpath("/html/body/label[1]/input")
        ele_user.click()
        action = ActionChains(self.driver)
        action.send_keys("Tom").pause(1)
        action.send_keys(Keys.SPACE).pause(1)
        action.send_keys("sd").pause(1)
        action.send_keys(Keys.BACK_SPACE).pause(1).perform()
        sleep(3)

if __name__ == '__main__':
    pytest.main(['-v','-s','test_ActionChains.py'])