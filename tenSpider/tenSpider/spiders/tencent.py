# -*- coding: utf-8 -*-
import scrapy
#load class CrawlSpider and Rule
from scrapy.spiders import CrawlSpider,Rule
#load the link rules to match satisfiled links
from scrapy.linkextractors import LinkExtractor 
from tenSpider.items import TenspiderItem 

class TencentSpider(CrawlSpider):
    name = 'tencent'
    allowed_domains = ['hr.tencent.com']
    start_urls = ['http://hr.tencent.com/position.php?&start=0#a']

    # the extract function in response,return a list match the rule

    pagelink=LinkExtractor(allow=("start=\d+"))
    
    #follow item will be used to Recursive crawling
    rules=[
        # get the link in pagelink, send the request one by one,
        # call the specified function to process 
        Rule(pagelink,callback="parseTencent",follow=True)
    ]
    # specified process function
    def parseTencent(self,response):
        for each in response.xpath("//tr[@class='even'] | //tr[@class='odd']"):
            item=TenspiderItem()
            #store the data into dict item
            #extract will transform the data into unicode string
            item['positionname']=each.xpath('./td[1]/a/text()').extract()[0]
            item['positionlink']=each.xpath('./td[1]/a/@href').extract()[0]
            item['positionType']=each.xpath('./td[2]/text()').extract()[0]
            item['peopleNum']=each.xpath('./td[3]/text()').extract()[0]
            item['workLocation']=each.xpath('./td[4]/text()').extract()[0]
            item['publishTime']=each.xpath('./td[5]/text()').extract()[0]

            yield item
