import requests
import time
from bs4 import BeautifulSoup
import re
import os
dirname = '图片'
os.mkdir(dirname)
url = 'http://moe.005.tv/moeimg/bz/'
headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'}
f_data = requests.get(url,headers=headers)
with open('f_html.txt','w',encoding='utf-8') as f:
    f.write(f_data.text)
with open('f_html.txt','r') as f:
    data1 = f.read()


p = re.compile('<a href=.*html" target="_blank">')
pic = re.findall(p,data1)
k = 0
k2 = 2000
for x in pic:
    s_data = requests.get(x[9:-18],headers=headers)
    with open('s_html.txt','w',encoding='utf-8') as f:
        f.write(s_data.text)
    with open('s_html.txt','r') as f:
        data2 = f.read()
    p1 = re.compile('<img alt="" src=.*/>')
    pic2 = re.findall(p1,data2)
    p2 = re.compile('http.*jpg')
    p3 = re.compile('http.{0,60}.png')
    
    for y in pic2:
        d = re.findall(p2,y)
        if d!=[]:
            s = requests.get(d[0])
            with open('%s/%s.jpg'%(dirname,k),'wb') as f:
                f.write(s.content)
            k = k + 1
    for z in pic2:
        d2 = re.findall(p3,z)
        if d2!=[]:
            s1 = requests.get(d2[0])
            with open('%s/%s.png'%(dirname,k2),'wb') as f:
                f.write(s1.content)
            k2 = k2 + 1
            