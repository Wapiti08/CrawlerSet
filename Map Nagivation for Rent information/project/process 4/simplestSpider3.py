from urllib import request

headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0;WOW64;rv:45)'}
url='http://example.webscraping.com'
req=request.Request(url,headers=headers)
response=request.urlopen(req)
print(response)

print(response.read().decode())