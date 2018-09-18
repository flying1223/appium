#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-09-04
# @Author  : flying


import HTMLTestRunner
import unittest
from appium import webdriver
import time



class Bangdan_Page_Test(unittest.TestCase):

    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '5.1'
        desired_caps['deviceName'] = 'NX511J'
        desired_caps['appPackage'] = 'com.Qunar'
        desired_caps['appActivity'] = 'com.mqunar.splash.SplashActivity'
        # 进入大客户端首页
        global driver
        driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        time.sleep(15)
        # 进入攻略城市页
        driver.find_element_by_id('com.mqunar.atom.alexhome:id/atom_alexhome_mod_gonglue').click()
        time.sleep(20)
        '''
        contexts = driver.contexts
        print contexts  #[u'NATIVE_APP', u'WEBVIEW_com.Qunar']
        driver.switch_to.context(contexts[1])
        '''
        # 进入榜单列表页
        driver.tap([(234, 786), (438, 834)], 100)
        time.sleep(15)

        # 进入榜单详情页
        driver.tap([(36, 516), (522, 1112)], 100)
        time.sleep(15)
    def tearDown(self):
        time.sleep(3)
        driver.quit()
#榜单名称
    def test_name(self):
        # driver1 = driver.tap([(0,825),(1080,1065)])
        # print (driver1)
        driver_1 = driver.find_element_by_android_uiautomator('new UiSelector().text("收藏|这辈子一定要去的八个博物馆")')
        self.assertEqual(driver_1.text,u'收藏|这辈子一定要去的八个博物')

    def test_biaoqian(self):
        # driver2 = driver.tap([(86,1079),(158,1128)])
        # print driver2
        driver_2 = driver.find_element_by_android_uiautomator('new UiSelector().text("北京")')
        self.assertEqual(driver_2.text,u'北京')

if __name__ == '__main__':
    testunit = unittest.TestSuite()
    testunit.addTest(Bangdan_Page_Test('test_name'))
    #testunit.addTest(Bangdan_Page_Test('test_biaoqian'))

    fp = open('result.html', 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,
                                           title=u'测试报告',
                                           description=u'用例执行情况：')
    runner.run(testunit)
    fp.close()

