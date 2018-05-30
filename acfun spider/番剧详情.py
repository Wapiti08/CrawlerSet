# 美丽汤的模块是一个解析爬取对象的模块
from bs4 import BeautifulSoup
# requests是从网页爬取数据的模块
import requests
import urllib.request
import csv
import time
import sys
from get_proxy import get_head
from get_proxy import get_ip

if len(sys.argv) >= 2:
    cur_page = int(sys.argv[1])
else:
    cur_page = 5020505

url = "http://www.acfun.cn/bangumi/aa{page}"
csv_file = open("opera.csv", "a+")
csv_writer = csv.writer(csv_file, delimiter=',')


while cur_page <= 10000000:
    
    print("scrapy: ", url.format(page=cur_page))
    # 定义user_agent
    head = get_head()
    # 定义代理ip
    proxy_addr = get_ip()
    # 设置代理
    proxy = urllib.request.ProxyHandler({'http': proxy_addr})
    # 创建一个opener
    # opener = urllib.request.build_opener(proxy, urllib.request.HTTPHandler)
    opener = urllib.request.build_opener(proxy)
    # 将opener安装为全局
    urllib.request.install_opener(opener)

    # 用urlopen打开网页
    # data = urllib.request.urlopen(url).read().decode('utf-8', 'ignore')
    # print('=================================================================')

    response = requests.get(url.format(page=cur_page), headers=head)
    print(response)

    html = BeautifulSoup(response.text, 'html.parser')

    movie_list = html.select("#main-info div")
    # print(movie_list)
    # if not movie_list:
    #     break

    num = 0

    for movie in movie_list:
        try:
            movie_picture = movie.select("div")[0].select("img")[0]["data-original"]      
            print("图片地址",movie_picture)
            # 抓取番剧名,播放量,追番数
            titles=html.select("#main-info #det-info")
            # if not titles:
            #     break
            for title in titles:
                movie_title=title.select('div')[0].select('span')[0].string
                print("番剧名:",movie_title)
            show_nums=title.select('p')[0].select('span')[1].string
            print("总播放量:",show_nums)
            constant_numbers=title.select('p')[0].select('span')[3].string
            print("追番数:",constant_numbers)
            
            #抓取标签
            labels=html.select("#main-info #det-info .tag")
            # if not labels:
            #     break
            
            for label in labels:
                movie_label1 = label.select("a")[0].select('div')[0].string
                print("标签:",movie_label1)
                try:
                    movie_label2 = label.select("a")[1].select('div')[0].string
                    movie_label3 = label.select("a")[2].select('div')[0].string
                    print(movie_label2,movie_label3)
                except:
                    continue
            
           #抓取简介
            comments=html.select("#main-info #det-info .describe")
            # if not comments:
            #     break
            for comment in comments:
                movie_comments=comment.select('p')[0].string
                print(movie_comments)
            time.sleep(1)
            #存入数据
            num += 1
            print(num)
            print("*********************")
            csv_writer.writerow([movie_picture, movie_title, show_nums, \
                    constant_numbers,movie_label1,movie_label2,movie_label3,movie_comments])
        except IndexError as e:
            print(e)

    cur_page += 1

    time.sleep(0.6)

csv_file.close()


