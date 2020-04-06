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
browser.get('http://sa.sogou.com/new-weball/page/sgs/epidemic?type_page=pcpop')
time.sleep(1)
browser.find_element_by_xpath("//li[@id='tab-column_3']/a").click()
i=0
while i<270:
        browser.find_element_by_xpath('//a[@data-action="viewMore"]').click()
        i=i+1

selector=Selector(text=browser.page_source)
tablelist=selector.xpath('//table[@id="trafficList"]/tbody/tr')
for one_message in tablelist:
        href=one_message.xpath('td[5]/span/a/@href').get()
        print(href)
        browser.get(href)
        selector2 = Selector(text=browser.page_source)
        text = selector2.xpath('//p')
        if 'wjw.nmg.gov.cn/' in href :
                for p in text:
                        word = p.xpath('span/span/text()').get()
                        print(word)
        elif 'shanxi.gov.cn' in href:
                text = selector2.xpath('//div[@class="ze-art"]')
                word = text[0].xpath('string(.)').get()
                print(word)
        elif 'hlj.gov.cn' in href :
                for p in text:
                        word = p.xpath('span/text()').get()
                        print(word)
        elif 'yn.gov.cn' in href:
                text=selector2.xpath('//div[@id="content"]')
                word = text[0].xpath('string(.)').get()
                print(word)
        elif 'http://www.beijing.gov.cn/' in href:
                text = selector2.xpath('//div[@class="TRS_Editor"]')
                word = text[0].xpath('string(.)').get()
                print(word)
        elif 'http://wjw.beijing.gov.cn/' in href:
                try:
                        text = selector2.xpath('//div[@class="article"]')
                        word = text[0].xpath('string(.)').get()
                        print(word)
                except:
                        text = selector2.xpath('//div[@class="weinei_left_con_sanji"]')
                        word = text[0].xpath('string(.)').get()
                        print(word)
        elif 'jl.gov.cn' in href:
                text = selector2.xpath('//div[@class="TRS_Editor"]')
                word = text[0].xpath('string(.)').get()
                print(word)

        elif 'http://wsjsw.qingdao.gov.cn/' in href:
                text = selector2.xpath('//div[@class="neirong-wz"]')
                word = text[0].xpath('string(.)').get()
                print(word)

        elif  'weibo.com' in href:
                continue
        elif 'weixin.qq.com' in href :
                try:
                        text = selector2.xpath('//section[@data-role="paragraph"]')
                        word = text[0].xpath('string(.)').get()
                        print(word)
                except:
                        text = selector2.xpath('//div[@class="rich_media_content "]')
                        word = text[0].xpath('string(.)').get()
                        print(word)

        elif 'https://mp.weixin.qq.com/s/IuDKcLAMgWZJ89ecl4dTcg' in href:
                text = selector2.xpath('//div[@class="rich_media_content"]')
                word = text[0].xpath('string(.)').get()
                print(word)

        elif 'http://wjw.shanxi.gov.cn/wjywl02/25329.hrh' in href:
                text = selector2.xpath('//div[@class="ze-art"]')
                word = text[0].xpath('string(.)').get()
                print(word)

        elif 'http://www.bjnews.com.cn/feature/2020/03/11/702168.html' in href:
                text = selector2.xpath('//div[@class="content"]')
                word = text[0].xpath('string(.)').get()
                print(word)

        elif 'http://wsjk.tj.gov.cn/art/2020/3/25/art_87_72720.html' in href:
                text = selector2.xpath('//div[@class="page_content Clear"]')
                word = text[0].xpath('string(.)').get()
                print(word)

        elif 'http://www.gzhfpc.gov.cn/xwzx_500663/tzgg/202003/t20200329_55695466.html' in href:
                text = selector2.xpath('//div[@class="view TRS_UEDITOR trs_paper_default trs_word trs_key4format"]')
                word = text[0].xpath('string(.)').get()
                print(word)

        elif 'http://ynswsjkw.yn.gov.cn/wjwWebsite/web/doc/UU158568321265357625' in href:
                text = selector2.xpath('//div[@class="fb_day"]')
                word = text[0].xpath('string(.)').get()
                print(word)

        else:
                for p in text:
                        word=p.xpath('text()').get()
                        print(word)

        time.sleep(2)

browser.close()
