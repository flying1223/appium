#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-09-0
# @Author  : flying

from appium import webdriver
import time

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '5.1'
desired_caps['deviceName'] = 'NX511J'
desired_caps['appPackage'] = 'com.Qunar'
desired_caps['appActivity'] = 'com.mqunar.hy.browser.activity.HyWebActivity01'  #'com.mqunar.splash.SplashActivity'

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
time.sleep(15)
