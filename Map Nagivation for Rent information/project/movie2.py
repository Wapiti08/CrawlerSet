# 美丽汤的模块是一个解析爬取对象的模块
from bs4 import BeautifulSoup
# requests是从网页爬取数据的模块
import requests
import csv
import re
import time
import sys
import random

if len(sys.argv) >= 2:
    cur_page = int(sys.argv[1])
else:
    cur_page = 0


url = "http://maoyan.com/cinemas?offset={page}"
csv_file = open("movie.csv", "a+")
csv_writer = csv.writer(csv_file, delimiter=',')
# cur_page = 1

'''List = ['Mozilla/5.0 (Windows NT 6.2; WOW64; rv:21.0) Gecko/20100101 Firefox/21.0', \
        'Mozilla/5.0 (Android; Mobile; rv:14.0) Gecko/14.0 Firefox/14.0', \
        'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.94 Safari/537.36', \
        'Mozilla/5.0 (Linux; Android 4.0.4; Galaxy Nexus Build/IMM76B) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.133 Mobile Safari/535.19', \
        'Mozilla/5.0 (iPad; CPU OS 5_0 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9A334 Safari/7534.48.3', \
        'Mozilla/5.0 (iPod; U; CPU like Mac OS X; en) AppleWebKit/420.1 (KHTML, like Gecko) Version/3.0 Mobile/3A101a Safari/419.3', \
        'Mozilla/5.0 (Linux; Android 4.1.1; Nexus 7 Build/JRO03D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Safari/535.19', \
        'Mozilla/5.0 (Linux; U; Android 4.0.4; en-gb; GT-I9300 Build/IMM76D) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30', \
        'Mozilla/5.0 (Linux; U; Android 2.2; en-gb; GT-P1000 Build/FROYO) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1']'''

while cur_page <= 10:
    
      
    '''i = random.randint(0, len(List) - 1)'''
    
    print("scrapy: ", url.format(page=cur_page*12))

    head = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.2; WOW64; rv:21.0) Gecko/20100101 Firefox/21.0'}

    response = requests.get(url.format(page=cur_page), headers=head)

    
    html = BeautifulSoup(response.text, 'html.parser')
   
    movie_list = html.select("#app div.cinemas-list")
    
    if not movie_list:
        break

    for movie in movie_list:
        try:
            movie_address = movie.select("div")[0].select('p')[0].string.strip()
            
            print("*********************")
            csv_writer.writerow(movie_address)
        except IndexError as e:
            print(e)

    cur_page += 1

    '''i += 1'''

    time.sleep(1)

csv_file.close()


