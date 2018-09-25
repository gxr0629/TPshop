from appium import webdriver


def web_driver():
    desired_caps = dict()
    # 设备信息
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '5.1'
    desired_caps['deviceName'] = '192.168.56.101:5555'
    # app信息
    desired_caps['appPackage'] = 'com.tpshop.malls'
    desired_caps['appActivity'] = '.SPMainActivity'
    desired_caps['automationName'] = 'Uiautomator2'

    return webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
