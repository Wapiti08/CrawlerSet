'''
爬虫大概包括四部分：
1.获取网页 requests
2.提取数据 
3.过滤数据
'''
#美丽汤的模块是一个解析爬取对象的模块
from bs4 import BeautifulSoup
#requests是从网页爬取数据的模块
import requests
import csv
import re
import time
import sys

if len(sys.argv) >= 2:
	cur_page = int(sys.argv[1])
else:
	cur_page = 2

url = "http://zu.wuhan.fang.com/house/i3{page}/"
csv_file = open("wuhan.csv", "a+")
csv_writer = csv.writer(csv_file,delimiter=',')
#cur_page = 1

while cur_page <= 10:
	print("scrapy: ", url.format(page=cur_page))

	response = requests.get(url.format(page=cur_page))

	html = BeautifulSoup(response.text,"html.parser")

	house_list = html.select("#houselistbody>#div.listBox>div.houseList")

	if not house_list:
		break

	num = 0

	for house in house_list:
		try:
			house_title = house.select("dl")[0].select("dd")[0].select("a")[0].string.strip()
			house_url = house.select("dl")[0].select("dd")[0].select("a")[0]["href"]
			house_location = \
			house.select("dl")[0].select("dd")[0].select("p")[2].select("span")[0].string.strip()
			house_money = house.select("dl")[0].select("dd")[0].select("div")[1].select("span")[0].string.strip()
			num += 1
			print(house_title)
			print(house_url)
			print(house_location)
			print(house_money)
			print(num)
			print("*********************")
			csv_writer.writerow([house_title,house_location,house_money,house_url])
		except IndexError as e:
			print(e)

	cur_page +=1

	time.sleep(2)

csv_file.close()


