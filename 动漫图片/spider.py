import requests
from bs4 import BeautifulSoup
import re
url0 = 'https://www.52dmtp.com/tags/514.html'
headers= {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'}
data = requests.get(url0,headers=headers)
soup = BeautifulSoup(data.text.encode('utf-8'),'lxml')
first = soup.find_all('a',class_='picLink tupian')
k = 0
for x in first:
    url1 = x.get('href')
    data1 = requests.get(url1,headers=headers)
    pattern_s = re.compile('<img src="http.*800".*>')
    
    p = re.findall(pattern_s,data1.content.decode('utf-8'))
    for i in p:
        soup2 = BeautifulSoup(i,'lxml')
        pic = soup2.find('img')
        second = requests.get(pic.get('src'),headers=headers)
        with open('%s.jpg'%k,'wb') as f:
            f.write(second.content)
    k=k+1