# -*- coding: utf-8 -*-
"""
Created on Fri May 18 14:14:51 2018

@author: Lenovo
"""

'''
猫眼网站top100的电影数据：
	http://maoyan.com/board/4?offset=0
	http://maoyan.com/board/4?offset=10
	http://maoyan.com/board/4?offset=20
	...
	http://maoyan.com/board/4?offset=90
'''

'''
有一些流程：
发起请求，得到响应过程
写入文件的部分
从网页中获取信息，包括电影名，主演和上映时间；
爬取多个页面同类型的信息
'''
import random
import re
import requests
import time
import json
#from multiprocessing import Pool


def  get_one_page(url):
	"""
	   发起Http请求，获取Response的响应结果
	"""
	user_agent = [\
		'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.94 Safari/537.36', \
		'Mozilla/5.0 (Linux; Android 4.0.4; Galaxy Nexus Build/IMM76B) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.133 Mobile Safari/535.19', \
		'Mozilla/5.0 (iPad; CPU OS 5_0 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9A334 Safari/7534.48.3', \
		'Mozilla/5.0 (iPod; U; CPU like Mac OS X; en) AppleWebKit/420.1 (KHTML, like Gecko) Version/3.0 Mobile/3A101a Safari/419.3', \
		'Mozilla/5.0 (Linux; Android 4.1.1; Nexus 7 Build/JRO03D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Safari/535.19', \
		]
	headers={'User-Agent':random.choice(user_agent)}
	response=requests.get(url,headers=headers)
	result=response.status_code
	if result==200:
		return response.text
	else:
		return None

def parse_one_page(html):
	"""
		从获取到的html页面中提取真实想要存储的数据：
		电影名，主演，上映时间
	"""
	patterns=re.compile('<p class="name">.*?title="([\s\S]*?)"[\s\S]*?<p class="star">([\s\S]*?)</p>[\s\S]*?<p class="releasetime">([\s\S]*?)</p>')
	items=re.findall(patterns,html)
	#yield在返回的时候会保存当前的函数执行状态
	for item in items:
		yield{
			'title':item[0].strip(),
			'actor':item[0].strip(),
			'time':item[0].strip()}
    
def write_to_file(item):
	'''
	把抓取到的数据写入本地文件
	'''
	with open("猫眼.txt","a",encoding='utf-8') as p:
		#jgon encode ->json str
		p.write(json.dumps(item,ensure_ascii=False)+'\n')


def CrawlMovieInfo(offset):
    """
    抓取电影的电影名，主演，上映时间
    """
    url = 'http://maoyan.com/board/4?offset='+str(offset)
    # 抓取当前的页面
    html = get_one_page(url)
    #print(html)
    
    for item in parse_one_page(html):
#        lock.acquire()
        write_to_file(item)
#        lock.release()
    
    # 每次下载完一个页面，随机等待1-3秒再次去抓取下一个页面
    time.sleep(random.randint(1,3))


if __name__=="__main__":
	#把页面做10次的抓取，每一个页面都是一个独立的入口
    for i in range(3):
        CrawlMovieInfo(i*10) #offset
        

