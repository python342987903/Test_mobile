from selenium.webdriver.common.by import By
from base.base import Base

class SearchPage(Base):
    def __init__(self,driver): # 子类重写父类初始化方法,传入的还是父类的driver驱动
        Base.__init__(self,driver)  # 强制调用执行父类方法
        # 抽取页面元素
        self.search_btn = (By.ID,"com.android.settings:id/search") # 搜索按钮
        self.search_input = (By.ID,"android:id/search_src_text") # 输入框
        self.results = (By.ID,"com.android.settings:id/title") # 搜索结果列表
    def click_search_btn(self):
        self.click_element(self.search_btn)  # 点击搜索按钮

    def send_search_text(self,text):
        self.send_element(self.search_input,text) # 输入数据
    def get_search_result(self):
        data = self.search_elements(self.results)
        return [i.text for i in data]
