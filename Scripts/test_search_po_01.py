import sys, os
sys.path.append(os.getcwd()) # 添加Python搜索路径
import allure
from base.initdriver import get_driver # 导入传入驱动方法
from page.search_page import SearchPage # 导入搜索页面元素方法
import pytest
class Test_SearchBase:
    def setup_calss(self):
        self.driver = get_driver('com.android.settings','.Settings') # 写死的属性
        self.search_obj = SearchPage(self.driver) # 实例化页面类

    def teardown_calss(self):
        self.driver.quit()

    @allure.step(title="点击搜索按钮")  # 应用在测试方法上方
    @pytest.fixture(scope='class',autouse=True)
    def click_search(self):
        self.search_obj.click_search_btn() # 点击搜索按钮不需要加test

    @allure.step(title="输入数据")  # 应用在测试方法上方
    def test_search_text(self,search_data,search_value):
        self.search_obj.send_search_text(search_data) # 输入数据
        assert search_value in self.search_obj.get_search_result() # 获取结果断言
if __name__ == "__main__":
    pytest.main()