from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class Base:
    def __init__(self,driver):
        self.driver = driver # 外传driver来初始化
        # loc=(定位类型,属性值)

    def search_elements(self,loc,timeout=15,poll_frequency=1):
        return WebDriverWait(self.driver,timeout,poll_frequency).until(lambda x: x.find_elements(*loc))
    def search_element(self,loc,timeout=15,poll_frequency=1):
        return WebDriverWait(self.driver,timeout,poll_frequency).until(lambda x: x.find_element(*loc))
    def click_element(self,loc,timeout=15,poll_frequency=1):
        self.search_element(loc,timeout,poll_frequency).click()
    def send_element(self,loc,text,timeout=15,poll_frequency=2):
        yuans = self.search_element(loc,timeout=15,poll_frequency=1)
        yuans.clear() # 先清空
        self.search_element(loc, timeout=15, poll_frequency=1).send_keys(text) # 输入数据