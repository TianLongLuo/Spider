import requests
from bs4 import BeautifulSoup

url = 'https://movie.douban.com/subject/25931446/'
headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'}
wb_data = requests.get(url,headers=headers)
soup = BeautifulSoup(wb_data.text,'lxml')
pattern = soup.find_all('span','short')
for item in pattern:
    with open('1.txt','a') as f:
        f.write(item.string + '\n\n')