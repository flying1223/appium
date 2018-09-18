#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-08-30
# @Author  : flying

from appium import webdriver
import time

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '5.1'
desired_caps['deviceName'] = 'NX511J'
desired_caps['appPackage'] = 'cn.nubia.calculator2.preset'
desired_caps['appActivity'] = 'cn.nubia.calculator2.Calculator'

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

time.sleep(1)
driver.find_element_by_id("cn.nubia.calculator2.preset:id/digit1").click()
time.sleep(1)
driver.find_element_by_id("cn.nubia.calculator2.preset:id/digit5").click()
time.sleep(1)
driver.find_element_by_id("cn.nubia.calculator2.preset:id/digit9").click()
time.sleep(1)
driver.find_element_by_id("cn.nubia.calculator2.preset:id/panelswitch").click()
time.sleep(1)
driver.find_element_by_id("cn.nubia.calculator2.preset:id/digit9").click()
time.sleep(1)
driver.find_element_by_id("cn.nubia.calculator2.preset:id/digit5").click()
time.sleep(1)
driver.find_element_by_id("cn.nubia.calculator2.preset:id/plus").click()
time.sleep(1)
driver.find_element_by_id("cn.nubia.calculator2.preset:id/digit6").click()
time.sleep(1)
driver.find_element_by_id("cn.nubia.calculator2.preset:id/equal").click()
time.sleep(1)
driver.quit()
