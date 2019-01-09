import urllib

def download1(url):
	'''最简单爬虫'''
	return urllib.request.urlopen(url).read()

def download2(url):
	'''捕获下载异常的爬虫'''
	print('Downloading',url)
	try:
		html=urllib.request.urlopen(url).read()
	except urllib.error.URLError as e:
		print('Download error',e.object)
		html=None
	return html

def download3(url,num_retries=2):
	'''捕获下载异常的爬虫并设定反复尝试上限的爬虫'''
	print('Downloading',url)
	try:
		html=urllib.request.urlopen(url).read()
	except urllib.error.URLError as e:
		print("Download error",e.object)
		html=None
		if num_retries>0:
			#判断错误码是否在500-600之间，是不是服务器错误
			if hasattr(e,'code') and 500<=e.code<600:
				html=download3(url,num_retries-1)
	return html



