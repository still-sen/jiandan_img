# -*- coding: utf-8 -*-
# @Time             : 2018/1/13 17:52
# @Author           : ws
# @project_name     : worm
# @File             : jiandan.py
# @Software         : PyCharm
#@belong to file    :  煎蛋妹子

from selenium import webdriver
import re

#定义请求地址url
url = "http://jandan.net/ooxx"

driver=webdriver.PhantomJS('../../phantomjs-2.1.1-windows/bin/phantomjs.exe')

driver.get(url)

# driver.save_screenshot('jiandan1.png')

#获取网页数据
url_list=[]

#得到第一页图片
for element in driver.find_elements_by_xpath("//div[@class='text']/p/img"):
    img_url = element.get_attribute('src')
    url_list.append(img_url)
print url_list

# 得到第一页的页数
p=driver.find_element_by_xpath("//div[@class='comments'][2]/div[@class='cp-pagenavi']/span[@class='current-comment-page']")
page=p.text

page=re.findall(r'\d+',page)[0]
print type(page)


page=int(page)
page = page - 1

while page>470:

    url='http://jandan.net/ooxx/page-'+str(page)+'#comments'

    driver = webdriver.PhantomJS('../../phantomjs-2.1.1-windows/bin/phantomjs.exe')

    driver.get(url)

    # 得到其他页图片
    for element in driver.find_elements_by_xpath("//div[@class='text']/p/img"):
        img_url = element.get_attribute('src')
        url_list.append(img_url)

    page=page-1

print url_list
print page

    # http://jandan.net/ooxx/page-475#comments
# //div[@class='comments'][2]/div[@class='cp-pagenavi']/span[@class='current-comment-page']

#获取网页数据
# for pic_url in picture:
#     print(">>>>>>>>>>>>开始保存图片%s" % pic_url)
    # response2 = requests.get(pic_url)
    #
    # #储存图片
    # filename = pic_url[-20]
    # with open("jd_img/" + filename,"wb") as f:
    #     f.write(response2.content)
    # print("<<<<<<<<<<<<保存完成")

