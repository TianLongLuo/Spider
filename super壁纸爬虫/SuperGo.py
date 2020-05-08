import requests
from bs4 import BeautifulSoup
import re
import os
from requests.exceptions import ReadTimeout,ConnectTimeout,ConnectionError,RequestException
#获取所有页数的地址
def TotalUrl(url,header):
    pages = 1
    while True:
        print('第%s页开始爬取'%pages)
        Allphoto(url,header,pages)
        print('第%s页爬取完毕'%pages)
        url_page_header = 'http://moe.005.tv/moeimg/bz/'
        next_url_data = requests.get(url,headers=header)
        next_url_factors = re.compile('list.*html.*class=\'n')
        next_url_factor = re.compile('list.*html')
        next_url_false = re.findall(next_url_factors,next_url_data.text)
        if next_url_false == []:
            break
        else:
            next_url = re.findall(next_url_factor, next_url_false[0])
            url = url_page_header+next_url[0]
            print('下一页地址获取成功')
            pages += 1
#获取第一页的相册地址
def Allphoto(url,header,pages):
    photoNum = 1
    allphoto_url_data = requests.get(url,headers=header)
    allphoto_factor = re.compile('http:.*v/\d{5,7}\.html')
    allphoto_url_data_soup = BeautifulSoup(allphoto_url_data.text,'lxml')
    allphoto_url_false = allphoto_url_data_soup.find('div',class_='zhuti_w_list')
    allphoto_url_false = str(allphoto_url_false)
    allphoto_url = re.findall(allphoto_factor,allphoto_url_false)
    i = 0
    for item in allphoto_url:
        if i == 0 :
            print('第%s页第%s个相册开始爬取' % (pages, photoNum))
            Photo(item,header,pages,photoNum)
            print('爬取完毕100%')
            photoNum += 1
            i = 1
        else:
            i = 0
#进入相册获取图片地址
def Photo(url,header,pages,photoNum):
    imageNum = 1
    k = 1
    while True:
        try:
            allImage_url_data = requests.get(url,headers=header,timeout=0.1)
            allImage_url_data_soup = BeautifulSoup(allImage_url_data.text,'lxml')
            allImage_url_false = allImage_url_data_soup.find('div',class_='content_nr')
            allImage_url_false = str(allImage_url_false)
            photo_factor = re.compile('http.{9,14}uploads/allimg.{21,30}\.jpg')
            allImage_url = re.findall(photo_factor,allImage_url_false)
            if allImage_url != []:
                for item in allImage_url:
                    print('第%s张图片地址获取成功' % imageNum)
                    DownloadImage(item,header,pages,photoNum,imageNum)
                    imageNum += 1
            k += 1
            url = url.replace('.html','')+'_%s'%k + '.html'
        except ReadTimeout as e:
            print('请求超时')
            break
        except ConnectTimeout as e:
            print('连接超时')
            break
        except ConnectionError as e:
            print('连接失败')
            break
        except RequestException as e:
            print('请求失败')
            break


#开始下载图片
def DownloadImage(url,header,pages,photoNum,imageNum):
    try:
        image = requests.get(url,headers=header,timeout=1)
        with open('图片/%s_%s_%s.jpg'%(pages,photoNum,imageNum),'wb') as f:
            f.write(image.content)
        print('下载成功')
    except ReadTimeout as e:
        print('请求超时')
    except ConnectTimeout as e:
        print('连接超时')
    except ConnectionError as e:
        print('连接失败')
    except RequestException as e:
        print('请求失败')
if __name__ == '__main__':
    os.mkdir('图片')
    url = 'http://moe.005.tv/moeimg/bz/'
    header = {
        'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'
    }
    TotalUrl(url,header)