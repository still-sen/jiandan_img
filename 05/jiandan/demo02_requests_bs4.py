# coding:utf-8

import requests
from bs4 import BeautifulSoup

#定义请求地址url
url = "http://jandan.net/ooxx"

#定义请求头
headers = {
    "Host":"jandan.net",
    "Upgrade-Insecure-Requests":"1",
    "Cookie":"_ga=GA1.2.489157472.1515827032; _gid=GA1.2.1638883040.1515827032",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.94 Safari/537.36"
}

#向指定url发送请求获取数据
response = requests.get(url,headers=headers)

#获取网页数据
soup = BeautifulSoup(response.text)
print soup


div_e = soup.select("div[class='text']")

print(div_e)

# for pic_url in picture:
#     print(">>>>>>>>>>>>开始保存图片%s" % pic_url)
    # response2 = requests.get(pic_url)
    #
    # #储存图片
    # filename = pic_url[-20]
    # with open("jd_img/" + filename,"wb") as f:
    #     f.write(response2.content)
    # print("<<<<<<<<<<<<保存完成")

'''
/html/body/div[@id='wrapper']/div[@id='body']/div[@id='content']/div[@id='comments']/ol[@class='commentlist']/li[@id='comment-3672717']/div/div[@class='row']/div[@class='text']/p/img/@src
'''