from bs4 import BeautifulSoup
import requests
import csv
import re
import time

url = "http://maoyan.com/cinemas?offset={page}"
csv_file = open("movie.csv", "a+")
csv_writer = csv.writer(csv_file,delimiter=',')
#cur_page = 1

cur_page=1

while cur_page <= 70:
	print("scrapy: ", url.format(page=cur_page*12))

	head='Mozilla/5.0 (Linux; Android 4.1.1; Nexus 7 Build/JRO03D) \
        AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Safari/535.19'

	response = requests.get(url.format(page=cur_page),headers=head)

	html = BeautifulSoup(response.text,'html.parser')

	movie_list = html.select(".container #post_container > li")

	if not movie_list:
		break

	num = 0

	for movie in movie_list:
		try:
			movie_title = movie.select("h2")[0].select("a")[0].string.strip()
			movie_url = movie.select("h2")[0].select("a")[0]["href"]
			movie_time = \
			movie.select(".info")[0].select('span')[0].string.strip()
			movie_comments_numbers = movie.select(".info")[0].select('span')[2].string.strip()
			num += 1
			print(movie_title)
			print(movie_url)
			print(movie_time)
			print(movie_comments_numbers)
			print(num)
			print("*********************")
			csv_writer.writerow([movie_title,movie_url,movie_time,movie_comments_numbers])
		except IndexError as e:
			print(e)

	cur_page +=1

	time.sleep(2)

csv_file.close()


