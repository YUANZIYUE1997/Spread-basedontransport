import datetime
from functools import reduce

from selenium import webdriver
from scrapy import Selector
import time
import re
import string
import pymysql
from tqdm import tqdm
import json
import os
import requests
from selenium.webdriver import ActionChains

headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'}

chrome_options = webdriver.ChromeOptions()
# 配置不加载图片
prefs = {"profile.managed_default_content_settings.images": 2}
chrome_options.add_experimental_option("prefs", prefs)
# 配置无头浏览器
chrome_options.add_argument('--headless')

browser = webdriver.Chrome(executable_path='C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe')

# 打开登陆页面
browser.get('http://qianxi.baidu.com/')
time.sleep(3)

browser.find_element_by_xpath('//span[@class="cur_city_name"]').click()
browser.find_element_by_xpath('//a[@name="武汉"]').click()
browser.find_element_by_xpath('''//span[@class="hui-option-tips"]'''). click()
browser.find_element_by_xpath('//a[@hui-option-tips="2020-03-29"]').click()
time.sleep(2)
selector = Selector(text=browser.page_source)
datas=selector.xpath('//table[@style="width: 100%; border-collapse: collapse; table-layout: fixed; text-align: center;"]/tbody/tr')
#print(datas)
for data in datas:
    city=data.css('span.mgs-date-city::text').get()
    province=data.css('span.mgs-date-province::text').get()
    rate=data.xpath('td[3]/text()').get()
    print(city,province,rate)
