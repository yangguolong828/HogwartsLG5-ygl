from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:



    def find(self, by, value):
        return self.driver.find_element(by=by, value=value)

    def __init__(self, driver: WebDriver = None):
        self.driver = driver