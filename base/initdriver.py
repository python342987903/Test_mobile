from appium import webdriver
def get_driver(pac,act):
    desired_caps = {}
    desired_caps['platformName'] = 'android'
    desired_caps['platformVersion'] = '5.1'
    desired_caps['deviceName'] = 'sunxin:5555'
    desired_caps['appPackage'] = pac
    desired_caps['appActivity'] = act
    return webdriver.Remote("http://127.0.0.1:4723/wd/hub",desired_caps)
