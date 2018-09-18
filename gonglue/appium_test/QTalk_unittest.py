#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-09-03
# @Author  : flying

import time
from appium import webdriver
import unittest
from QTalk_IOS_UITest import QTalkIOSTest
import HTMLTestRunner


class take_screen_shot():  # 这个类将在下面作为装饰器使用
    def __init__(self, func):
        self.func = func
        self.name = func.__name__ + ' (__main__.CalTestCase).png'  # 拼接截图文件名

    def __call__(self, *args):  # 对每次调用的函数都做截图操作
        try:
            self.func(self, *args)
        finally:
            driver.get_screenshot_as_file(self.name)


class IOSTest(unittest.TestCase):
    # @classmethod
    def setUp(self):  # 每个test case 启动设置
        # set up appium
        caps = {}
        caps["platformName"] = "ios"
        caps["platformVersion"] = "11.1"
        caps["deviceName"] = "iPhone 6"
        caps["app"] = "/Users/admin/Desktop/qtalk_appstore.app"
        caps["noReset"] = True
        caps["nativeInstrumentsLib"] = True
        # caps["automationName"] = "XCUITest"
        # caps["noSign"] = True
        # caps["--no-reset"] = True
        # caps["unicodeKeyboard"] = True
        # caps["resetKeyboard"] = True
        global driver
        driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.userName = "ping.xue"
        self.password = ""
        self.sessionName = "呼呼呼"
        driver.hide_keyboard()

    # @classmethod
    def tearDown(self):  # 每个test case 关闭设置
        time.sleep(2)
        driver.quit()

    # @take_screen_shot #此装饰器可以对test case 进行一次截图
    def textQTalk(self):
        qtalk = QTalkIOSTest(driver)
        qtalk.login("ping.xue", "")
        qtalk.openSession("呼呼呼")
        # qtalk.sendMessage("aaa text")
        qtalk.screenShot("aaa.png")
        qtalk.gobackVC()
        qtalk.openSession("QTalk iOS TEAM")
        qtalk.screenShot("bbb.png")
        # qtalk.sendMessage("aaa text")


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(IOSTest('textQTalk'))
    # unittest.TextTestRunner(verbosity=2).run(suite)
    # 测试报告
    timestr = time.strftime('%Y-%m-%d %X', time.localtime(time.time()))  # 本地日期时间作为测试报告的名字
    filename = '/Users/admin/Documents/Test-ZQ/report/' + timestr + '.html'  # 这个路径改成自己的目录路径
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(
        stream=fp,
        title='result',
        description='report'
    )
    runner.run(suite)
    fp.close()
