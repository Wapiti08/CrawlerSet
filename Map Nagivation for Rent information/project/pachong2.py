'''
目标网站：http://wh.ganji.com/fang1/o{page}/
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
	cur_page = 9

url = "http://wh.ganji.com/fang1/o{page}/"
csv_file = open("wuhan.csv", "a+")
csv_writer = csv.writer(csv_file,delimiter=',')
#cur_page = 1

while cur_page <= 10:
	print("scrapy: ", url.format(page=cur_page))

	response = requests.get(url.format(page=cur_page))

	html = BeautifulSoup(response.text,"html.parser")

	house_list = html.select(".f-main-list > .f-list.js-tips-list")

	if not house_list:
		break

	num = 0

	for house in house_list:
		try:
			house_title = house.select("dl")[0].select("dd")[0].select("a")[0].string.strip()
			house_url = house.select("dl")[0].select("dd")[0].select("a")[0]["href"]
			house_location = \
			house.select("dl")[0].select("dd")[2].select("a")[2].string.strip()
			house_money = house.select("dl")[0].select("dd")[4].select("span")[0].string.strip()
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


