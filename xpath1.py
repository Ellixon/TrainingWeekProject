#-*- codeing =utf-8 -*- 
#@Time : 2020/10/26  
#@Author : lzl
#@File : xpath1.py
#@Software : PyCharm

import requests
from lxml import etree
from bs4 import BeautifulSoup


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.113 Safari/537.36'}

url='forum.php?mod=viewthread&tid=1108591&extra=page%3D1'

page_text=requests.get(url=url,headers=headers).text

tree=etree.HTML(page_text)
li_list=tree.xpath('//ul[@class="list"]/li')


fp=open('58.text','w',encoding='utf-8')
for li in li_list:
    title= li.xpath('./div[2]/h2/a/text()')[0]
    print(title)
    fp.write(title+'\n')