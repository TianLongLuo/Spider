import requests
from bs4 import BeautifulSoup

#请在这里输入总页数噢亲
total = 3
k = 1
while k <= total:
    #请在这儿输入带有页的网址噢，然后把数字改成%s一下
    url = 'https://tieba.baidu.com/p/6537947962?pn=%s'%total
    html_data = requests.get(url)
    soup = BeautifulSoup(html_data.text,'lxml')
    book_texts = soup.find_all('div',class_='d_post_content j_d_post_content')
    i = 0
    for x in book_texts:
        with open('all.txt','a+',encoding='utf-8') as f:
            f.write(book_texts[i].get_text())
            f.write('\n\n')
        i += 1
    print('第%s页爬取完毕'%k)
    k += 1