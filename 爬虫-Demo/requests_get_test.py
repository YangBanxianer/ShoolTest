#  -*- coding:utf-8 -*-
import requests
from bs4 import  BeautifulSoup
if __name__=='__main__':
    #将url用变量target绑定,方便之后调用
    target= 'http://www.biqukan.com/'
    #用get方法请求url中的htmml界面
    req = requests.get(url=target)
    text=req.text
    soup=BeautifulSoup(text)
    mydiv=soup.find_all('div',class='shoutxt')
    texts=mydiv[0].text.replace('\xao'*8,'\n\n')