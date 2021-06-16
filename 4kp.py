#-*- codeing =utf-8 -*- 
#@Time : 2020/10/28  
#@Author : lzl
#@File : 4kp.pydd
#@Software : PyCharm 

import requests
from lxml import etree
import os

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.113 Safari/537.36'}

url='http://pic.netbian.com/4kmeinv/index_%d.html'
pagenum=2
if pagenum<=6:
    pagenum+=1
    new_url=format(url%pagenum)

# for pagenum in range(2,9):
#     new_url = format(url%pagenum)
response=requests.get(url=new_url,headers=headers)
page_text=response.text
tree=etree.HTML(page_text)
li_list=tree.xpath('//div[@class="slist"]/ul/li')

#创建一个文件夹
if not os.path.exists('./piclibs'):
    os.mkdir('./piclibs')

#遍历循环保存
for li in li_list:
    img_src='http://pic.netbian.com/'+li.xpath('./a/img/@src')[0]
    img_name=li.xpath('./a/img/@alt')[0]+'.jpg'

    #名字乱码处理
    img_name1=img_name.encode('iso-8859-1').decode('gbk')

    #此代码段结果打印测试
    #print(img_name1)

    #请求图片，持久化存储
    img_data=requests.get(url=img_src,headers=headers).content
    img_path='piclibs/'+img_name1
    with open(img_path,'wb')as fp:
        fp.write(img_data)
        print(img_name1,'Download successful！！！')