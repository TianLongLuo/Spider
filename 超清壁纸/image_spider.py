import requests
from bs4 import BeautifulSoup
import os
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import InvalidElementStateException,WebDriverException


def setDownload():
    options = webdriver.ChromeOptions()
    prefs = {'profile.default_content_settings.popups':0,
             'download.default_directory':r'C:\Users\20696\Desktop\fuck_img'}
    options.add_experimental_option('prefs',prefs)
    driver = webdriver.Chrome(chrome_options=options)
    return driver

def getVideoUrl(url):
    driver = setDownload()
    driver.get(url)
    driver.implicitly_wait(20)
    for i in range(1000):
        try:
            print('第%s张图片爬取中 '%i,end='')
            above = driver.find_elements_by_css_selector('.img-box')[i]
            ActionChains(driver).move_to_element(above).click(above).perform()
            time.sleep(4)
            above2 = driver.find_element_by_css_selector('.download')
            ActionChains(driver).move_to_element(above2).click(above2).perform()
            above3 = driver.find_element_by_css_selector('.close')
            ActionChains(driver).move_to_element(above3).click(above3).perform()
            print('第%s张图片爬取完毕' %i)
        except InvalidElementStateException as e:
            print('广告位')
        except WebDriverException as e:
            print('广告位')

    os.system('pause')

if __name__ == '__main__':
    url = 'https://bz.zzzmh.cn/#anime'
    header = {
        "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36",
    }
    dirs = r'C:\Users\20696\Desktop\fuck_img'
    if not os.path.exists(dirs):
        os.mkdir(dirs)
    getVideoUrl(url)