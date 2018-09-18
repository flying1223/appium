#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-09-03
# @Author  : flying

import time
from appium import webdriver
import unittest
import HTMLTestRunner

class City_page_test(unittest.TestCase):

    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '5.1'
        desired_caps['deviceName'] = 'NX511J'
        desired_caps['appPackage'] = 'com.Qunar'
        desired_caps['appActivity'] = 'com.mqunar.splash.SplashActivity'

        global driver
        driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        time.sleep(15)
        driver.find_element_by_id('com.mqunar.atom.alexhome:id/atom_alexhome_mod_gonglue').click()
        time.sleep(15)

    def tearDown(self):
        time.sleep(2)
        driver.quit()

    def testcase(self):
        # try:
        contexts = driver.contexts
        #print contexts  #[u'NATIVE_APP', u'WEBVIEW_com.Qunar']
        driver.switch_to.context(contexts[1])
        driver1 = driver.find_element_by_xpath("//div[contains(text(),'酒店')]")

        self.assertEqual(driver1.text,u'酒店')


if __name__ == '__main__':
    print ('开始了------------')
    testunit = unittest.TestSuite()
    testunit.addTest(City_page_test('testcase'))

    fp = open('result.html','wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream = fp,
                                           title = u'测试报告',
                                           description = u'用例执行情况：')
    runner.run(testunit)
    print ('---ok---')
    fp.close()
