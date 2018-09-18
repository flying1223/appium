#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-09-03
# @Author  : flying

import time
from selenium.webdriver.common.keys import Keys


class QTalkIOSTest(object):

    def __init__(self, driver):
        self.driver = driver

    def login(self, userName, password):
        # login qtalk
        try:
            userTextField = self.driver.find_element_by_accessibility_id("请输入用户名")
            if userTextField:
                userTextField.send_keys(userName)
            # 获取验证码
            btnGetAuthCode = self.driver.find_element_by_accessibility_id("验证码")
            if btnGetAuthCode:
                btnGetAuthCode.click()
            time.sleep(10)
        except Exception, e:
            print '未出现登录界面'

    def logout(self):
        # 退出 qtalk
        print "logout"

    def checkLoginState(self):
        try:
            nav_bar = self.driver.find_element_by_class_name("XCUIElementTypeNavigationBar")
        except Exception, e:
            print e

    def openSession(self, sessionName):
        # 打开某个会话
        # time.sleep(10)
        try:
            # 切换到会话列表窗口
            self.driver.find_element_by_id("menu session").click()
            table = self.driver.find_element_by_class_name("XCUIElementTypeTable")
            nameLabel = table.find_element_by_id(sessionName)
            self.driver.scroll(table, nameLabel)
            nameLabel.click()
        except Exception, e:
            print "打开会话窗口失败"
            print e

    def gobackVC(self):
        # nav_bar = self.driver.find_element_by_class_name("XCUIElementTypeNavigationBar")
        # backBtn = nav_bar.find_elements_by_class_name("XCUIElementTypeButton")[0]
        # backBtn.click()
        # time.sleep(1)
        self.driver.back()

    def sendMessage(self, text):
        # 发送消息
        input = self.driver.find_element_by_accessibility_id("Enter what you have to say.")
        input.set_value(text)
        input.set_value(Keys.ENTER)

    def screenShot(self, file_name):
        time.sleep(1)
        ret = self.driver.get_screenshot_as_file(filename=file_name)
        if ret:
            print "截图成功"
        else:
            print "截图失败"