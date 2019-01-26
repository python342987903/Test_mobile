from selenium.webdriver.common.by import By

from base.base import Base
from appium import webdriver
import pytest
class Test_searchBase:
    def setup_class(self):
        desired_caps = {}
        desired_caps['platformName'] = 'android'
        desired_caps['platformVersion'] = '5.1'
        desired_caps['deviceName'] = 'shoujiming'
        desired_caps['appPackage'] = 'com.android.settings'
        desired_caps['appActivity'] = '.Settings'
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",desired_caps)#声明driver对象
        self.base_obj = Base(self.driver)  # 实例化base类,原驱动带self所以现在也带
        # 抽出页面元素
        self.search_btn = (By.ID,"com.android.settings:id/search") # 搜索按钮
        # 输入框
        self.search_input = (By.ID, "android:id/search_src_text")
        # 结果列表
        self.results = (By.ID, "com.android.settings:id/title")

    def teardown_class(self):
        self.driver.quit()
    @pytest.fixture(scope='class',autouse=True) # 自动运行一次
    def click_search_btn(self):
        self.base_obj.click_element(self.search_btn) # 调用base类中的点击方法
    # 动态传入遍历执行数据
    @pytest.mark.parametrize("search_data,search_value",[('1','休眠'),('m','MAC地址'),('w','WLAN直连')])
    def test_search_value(self,search_data,search_value):
        self.base_obj.send_element(self.search_input,search_data) # 输入内容
        result_data = self.base_obj.search_elements(self.results) # 搜索结果列表
        assert search_value in [i.text for i in result_data] # 与传入的预期文本对比断言

if __name__ == "__main__":
    pytest.main(['test_search_base.py'])