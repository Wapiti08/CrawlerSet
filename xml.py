from lxml import etree
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
