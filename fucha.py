import requests
from bs4 import BeautifulSoup


 response=requests.get(url+"https://weibo.com/p/1006051192329893/home?profile_ftype=1&is_all=1#_0")

soup=BeautifulSoup(response.text,features="html.parser")
target=