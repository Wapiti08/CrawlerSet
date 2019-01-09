from bs4 import BeautifulSoup
import requests
import csv
import time

#url = "https://dianying.nuomi.com/cinema/"
url = "https://dianying.nuomi.com/movie/movielist"

csv_file = open("movieadd.csv", "a+")
csv_writer = csv.writer(csv_file, delimiter=',')

cur_page = 0

while cur_page <= 0:
    print("scrapy: ", url)
    head = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.2; WOW64; rv:21.0) Gecko/20100101 Firefox/21.0'}

    response = requests.get(url, headers=head)

    print(response.text)

    html = BeautifulSoup(response.text, 'html.parser')

    #print(html)

    movie_list = html.select(".widget-cinema-cinema-filter")
    print(movie_list)
    if not movie_list:
        break

    num = 0

    # for movie in movie_list:
    #
    #     #print(movie)
    #     #print("*************")
    #     try:
    #         print(movie)
    #         print('*********')
    #         cinema = movie.select('li')[0].select('div')[0].select('span')[0].string.strip()
    #         print(cinema)
    #         movie_add = movie.select('li')[0].select('div')[0].select('span')[1].string.strip()
    #         num += 1
    #         print(movie_add)
    #         print(num)
    #         print("*********************")
    #         csv_writer.writerow([cinema, movie_add])
    #     except IndexError as e:
    #         print(e)
cur_page += 1

time.sleep(1)

csv_file.close()


