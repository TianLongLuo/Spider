import requests
from bs4 import BeautifulSoup
url = 'https://tieba.baidu.com/p/6095449140'
headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'}
data = requests.get(url)
soup = BeautifulSoup(data.text,'lxml')
p = soup.find_all('img','BDE_Image')
k=0
for x in p:
    with open('%s.jpg'%k,'wb') as f:
        u = requests.get(x.get('src'))
        f.write(u.content)
    k=k+1