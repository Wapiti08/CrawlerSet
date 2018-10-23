from bs4 import BeautifulSoup
# requests是从网页爬取数据的模块
from urllib import request
import requests
import csv
import re
import time

url = 'http://www.xicidaili.com/'

csv_file = open('ip.csv', 'a+')

csv_writer = csv.writer(csv_file, delimiter=',')

ord = 0

while ord <= 1:
    print('scrapy:', url)

    head = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.2; WOW64; rv:21.0) Gecko/20100101 Firefox/21.0'}

    response = requests.get(url, headers=head)

    html = BeautifulSoup(response.text, 'html.parser')

    ip_list = html.select('#wrapper div.main #ip_list tr')
    # print(ip_list)
    if not ip_list:
        break

    i = 0
    num1 = 0
    for ip in ip_list:
        try:
            num1+=1
            # ip_port = ip.select('tr')[0]
            # print(ip_port)
            if num1>2:
                ip_ip = ip.select('td')[1].string.strip()
                ip_port = ip.select('td')[2].string.strip()
                print(ip_ip)
                print(ip_port)
            # ip_ip=ip.select('tr')[2]
            # ip_ip1=ip.select('tr')[4]
            # ip_ip=ip.select('tr')[ord]
            # ip_ip=ip.select('tr')[ord].select('td')[1].string.strip()
            # ip_port=ip.select('tr')[ord].select('td')[2].string.strip()
                i += 1
            # print(ip_ip)
            # print(ip_ip1)
            # print(ip_port)
                print(i)
                print('***************')
            else:
                continue
            csv_writer.writerow([ip_ip,ip_port])
        except IndexError as e:
            print(e)

    time.sleep(1)

    ord += 1

csv_file.close()

