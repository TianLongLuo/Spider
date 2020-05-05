import requests
from requests.exceptions import ReadTimeout,ConnectionError,RequestException,ConnectTimeout
from bs4 import BeautifulSoup
import os
import time
#获取相册集地址
def HomePic(url,header):
    i = 0
    fronturl = 'https://cn.pornhub.com'
    Photos = requests.get(url,headers=header)
    Photo_page = BeautifulSoup(Photos.text,'lxml')
    Photo_url = Photo_page.find_all(class_ = 'photoAlbumListBlock js_lazy_bkg')
    for x in Photo_url:
        innerurl = fronturl + (x.a.get('href'))
        innerPic(innerurl,header,i)
        i = i+1
#获取相册内图片地址
def innerPic(url,header,num):
    j = 0
    fronturl = 'https://cn.pornhub.com'
    Photos = requests.get(url,headers=header)
    Photo_page = BeautifulSoup(Photos.text,'lxml')
    Photo_url = Photo_page.find_all(class_='js_lazy_bkg photoAlbumListBlock')
    for x in Photo_url:
        basepicurl = fronturl + (x.a.get('href'))
        DownloadPic(basepicurl,header,num,j)
        j = j+1
#开始下载图片
def DownloadPic(url,header,n1,n2):
    k = 1
    time.sleep(1)
    try:
        homeImage = requests.get(url,headers=header,timeout=3)
        Image_page = BeautifulSoup(homeImage.text,'lxml')
        Image_url = Image_page.find_all('div',class_='centerImage')
        print('链接获取成功',end=' ')
        imageUrl = Image_url[k].img.get('src')
        image = requests.get(imageUrl)
        with open('images/%s_%s.jpg' % (n1, n2), 'wb') as f:
            f.write(image.content)
        global total
        total = total+1
        print('图片爬取成功 已爬取%s张'%total)
    except ReadTimeout as e:
        print('请求超时')
    except ConnectTimeout as e:
        print('连接超时')
    except ConnectionError as e:
        print('连接失败')
    except RequestException as e:
        print('请求失败')
    except AttributeError as e:
        print('属性错误')
    except IndexError:
        try:
            homeImage = requests.get(url, headers=header, timeout=2)
            Image_page = BeautifulSoup(homeImage.text, 'lxml')
            Image_url = Image_page.find_all('div', class_='centerImage')
            print('链接获取成功',end=' ')
            imageUrl = Image_url[k].img.get('src')
            image = requests.get(imageUrl)
            with open('images/%s_%s.jpg' % (n1, n2), 'wb') as f:
                f.write(image.content)
            total = total + 1
            print('图片爬取成功 已爬取%s张' % total)
        except ReadTimeout as e:
            print('请求超时')
        except ConnectTimeout as e:
            print('连接超时')
        except ConnectionError as e:
            print('连接失败')
        except RequestException as e:
            print('请求失败')
        except AttributeError as e:
            print('属性错误')
        except IndexError:
            print('没这个东西')


if __name__ == "__main__":
    total = 0
    #输入要爬取图片的网站
    home_url = 'https://cn.pornhub.com/albums/female-straight-uncategorized?search=%E5%85%A8%E5%8C%85'
    header = {
        'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36'
    }
    os.mkdir('images')
    HomePic(home_url,header)
