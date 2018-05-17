from lxml import etree
import requests

xml='''<bookstore>
<book>
    <title lang='en'>Harry Potter</title>
    <author>J K.Rowling</author>
    <year>2005</year>
    <price>29.99</price>
</book>
<book>
    <title lang='ch'>python 爬虫</title>
    <author>J.P Rowling</author>
    <year>2015</year>
    <price>39.99</price>
</book>
</bookstore>
'''


root=etree.fromstring(xml)
'''
print(root)
#获取book节点
elementsBook=root.xpath("book")
print(elementsBook)
elementAuthor=root.xpath("./book")
print(elementAuthor)
#获取title
elementsBook=root.xpath('book/title')
print(elementsBook)
#获取title的lang属性
elements=root.xpath("//@lang")
print(elements)
#获取book中的price
elements=root.xpath("book/price")
print(elements)
'''

def info(object, spacing=10):
	"""
	 Print methods and doc strings. Take module, class,
	 dictionary, or string.
	"""
	# 遍历一遍object对象，把里面的可以被调用的方法提取出来
	methodList = [method for method in dir(object)
				  if not callable(getattr(object, method))]

	# 把要提取出来的方法以更好看的,多行变单行
	processFunc = lambda s: " ".join(s.split())

	# 让左端打印的是方法名称，右端打印的是方法的doc名称
	print('\n'.join(["%s %s" % (str(method.ljust(spacing)),
								processFunc(str(getattr(object, method).__doc__)))
					 for method in methodList]))



root=etree.fromstring(xml)
print(root)
'''
bookElement=root.xpath("book")
print(bookElement)

bookTitle=root.xpath('/title')
print(bookTitle)

#elements=root.xpath("book")
#print(elements)
#print(elements[0].tag)
#info(elements[0])
#print(elements[0].getchildren()[0].text)
'''
#elements=root.xpath("//title[@*]")
#print(elements)
#for it in elements:
#    print(it.text)
    
elements=root.xpath('/bookstore/book[price>35]/title')
print(elements[0].text)