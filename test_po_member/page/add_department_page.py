from selenium.webdriver.common.by import By

from test_po_member.page.base_page import BasePage
from test_po_member.page.contact_page_new import NewContactPage


class AddDepartmentPage(BasePage):

    #添加部门成功
    def add_department(self):
        self.driver.find_element(By.XPATH, "//*[@class='js_create_party']").click()
        self.driver.find_element(By.XPATH, "//*[@name='name']").send_keys("质量保障")
        self.driver.find_element(By.CSS_SELECTOR, ".js_toggle_party_list").click()
        self.driver.find_element(By.CSS_SELECTOR, '.js_party_list_container [id="1688851053681111_anchor"]').click()
        self.driver.find_element(By.XPATH, '//*[@id="__dialog__MNDialog__"]/div/div[3]/a[1]').click()
        return NewContactPage(self.driver)


    #添加部门失败
    def add_department_fail(self):
        self.driver.find_element(By.XPATH, "//*[@class='js_create_party']").click()
        self.driver.find_element(By.XPATH, "//*[@name='name']").send_keys("  ")
        self.driver.find_element(By.CSS_SELECTOR, ".js_toggle_party_list").click()
        self.driver.find_element(By.CSS_SELECTOR, ".jstree.jstree-5.jstree-default [id='688851053681111_anchor']").click()
        self.driver.find_element(By.CSS_SELECTOR, ".ww_btn_Blue").click()
        return NewContactPage(self.driver)

    #添加子部门成功
    def add_sdepartment(self):
        self.driver.find_element(By.XPATH, "//*[@class='js_create_party']").click()
        self.driver.find_element(By.XPATH, "//*[@name='name']").send_keys("质量保障")
        self.driver.find_element(By.CSS_SELECTOR, ".js_toggle_party_list").click()
        self.driver.find_element(By.CSS_SELECTOR, ".jstree.jstree-5.jstree-default [id='1688850854889588_anchor']").click()
        self.driver.find_element(By.CSS_SELECTOR, ".ww_btn_Blue").click()
        return NewContactPage(self.driver)

    #添加子部门失败
    def add_sdepartment_fail(self):
        self.driver.find_element(By.XPATH, "//*[@class='js_create_party']").click()
        self.driver.find_element(By.XPATH, "//*[@name='name']").send_keys("  ")
        self.driver.find_element(By.CSS_SELECTOR, ".js_toggle_party_list").click()
        self.driver.find_element(By.CSS_SELECTOR, ".jstree.jstree-5.jstree-default [id='1688850854889588_anchor']").click()
        self.driver.find_element(By.CSS_SELECTOR, ".ww_btn_Blue").click()
        return NewContactPage(self.driver)