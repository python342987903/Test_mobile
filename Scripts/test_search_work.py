import pytest
from appium import webdriver
# params遍历传参的函数构造
@pytest.fixture(params=[{'key':'1','value':'休眠'},
                        {'key':'m','value':'MAC地址'},
                        {'key':'w','value':'WLAN直连'}])
def search_data(request):
    return request.param
class Test_Search_Work:
    def setup_class(self):
        desired_caps = {}
        desired_caps['platformName'] = 'android'
        desired_caps['platformVersion'] = '5.1'
        desired_caps['deviceName'] = 'sunxin:5555'
        desired_caps['appPackage'] = 'com.android.settings'
        desired_caps['appActivity'] = '.Settings'
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)

    def teardown_class(self):
        self.driver.quit()
    @pytest.fixture(scope='class',autouse=True)
    def click_search_btn(self):  # 点击搜索按钮
        self.driver.find_element_by_id("com.android.settings:id/search").click()
    @pytest.mark.parametrize("search_data, search_value", [("1", "休眠"), ("m", "MAC地址"), ("w", "WLAN直连")])
    def test_search_wor_param(self,search_data,search_value):
        self.driver.find_element_by_id('android:id/search_src_text').send_keys(search_data) # 输入内容
        result = self.driver.find_elements_by_id('com.android.settings:id/title')
        assert search_value in [i.text for i in result]