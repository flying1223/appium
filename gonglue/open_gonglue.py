#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-09-03
# @Author  : flying

from appium import webdriver
import time

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '5.1'
desired_caps['deviceName'] = 'NX511J'
desired_caps['appPackage'] = 'com.Qunar'
desired_caps['appActivity'] = 'com.mqunar.splash.SplashActivity'
#进入大客户端首页
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
time.sleep(15)

scheme_url = 'hysdk.sniff.scheme + `://react/open?hybridId=in_gonglue_guide_rn&pageName=NtSmartPage&initProps=${encodeU' \
             'RIComponent(JSON.stringify({"param":{"book":"7089577"}}))}`'
driver.start_activity('com.Qunar','com.mqunar.react.base.stack.container.QReactNativeActivity1',optional_intent_arguments = scheme_url)

time.sleep(15)
print (666)




#进入攻略城市页
# driver.find_element_by_id('com.mqunar.atom.alexhome:id/atom_alexhome_mod_gonglue').click()
# time.sleep(20)
# '''
# contexts = driver.contexts
# print contexts  #[u'NATIVE_APP', u'WEBVIEW_com.Qunar']
# driver.switch_to.context(contexts[1])
# '''
# #进入榜单列表页
# driver.tap([(234,786),(438,834)],100)
# print ('1111111111')
# time.sleep(15)
# contexts = driver.contexts
# print contexts
#
# #进入榜单详情页
# driver.tap([(36,516),(522,1112)],100)

#driver.quit()
