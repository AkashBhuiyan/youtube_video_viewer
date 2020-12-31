from selenium import webdriver
import time
import random as rand

import requests
from bs4 import BeautifulSoup
from random import choice

def get_proxy():
    url = "https://www.sslproxies.org/"
    r = requests.get(url)

    soup = BeautifulSoup(r.content, 'html.parser')
    proxyList = list(map(lambda x: x[0]+':'+x[1], list(zip(map(lambda x: x.text, soup.findAll('td')[::8]), map(lambda x: x.text, soup.findAll('td')[1::8])))))
    return {"https": choice(proxyList)}

def get_driver_by_proxy(PROXY):
    firefox_options = webdriver.ChromeOptions()
    firefox_options.add_argument('--proxy-server=http://%s' % PROXY)

    firefox = webdriver.Chrome(chrome_options=firefox_options)
    return firefox


def button_click(driver):
    sign_in_button = driver.find_element_by_xpath('//*[@id="movie_player"]/div[24]/div[2]/div[1]/button')
    sign_in_button.click()

def get_video_by_web_driver(driver, url):
    driver.get(url)
    return driver

def watch_video(urlList, driver):
    for i, url in enumerate(urlList):
        driver = get_video_by_web_driver(driver, url=url)
        time.sleep(1)
        # if i == 0:
        #     button_click(driver) # 1st youtube link need to click the play button
        sleep_time = rand.randint(60, 62) # choose the random time -> 60 to 62 seconds playing time
        time.sleep(sleep_time)


if __name__ == '__main__':
    print("How many times you want to play the List of videos : ")
    counter = int(input())
    while(counter >= 0):
        proxy = get_proxy()
        firefox = get_driver_by_proxy(PROXY=proxy['https'])
        urlList = [
                    'https://www.whatismyip.com/',
                    'https://www.youtube.com/watch?v=2Vv-BfVoq4g',
                    'https://www.youtube.com/watch?v=EWdIElQUI_4']
        watch_video(urlList=urlList, driver=firefox)
        counter = counter - 1

        firefox.quit()



