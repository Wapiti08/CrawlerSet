# -*- coding: utf-8 -*-
import scrapy
from tencent.items import TencentItem

class TencentcareersSpider(scrapy.Spider):
    name = 'tencentCareers'
    allowd_domains = ['tencent.com']
    url='http://hr.tencent.com/position.php?&start='
    
    offset=0
    start_urls = [url+str(offset)+'#a']

    def parse(self, response):
        for each in response.xpath("//tr[@class='even'] | //tr[@class='odd']"):
            item=TencentItem()
            #store the data into dict item
            #extract will transform the data into unicode string
            item['positionname']=each.xpath('./td[1]/a/text()').extract()[0]
            item['positionlink']=each.xpath('./td[1]/a/@href').extract()[0]
            item['positionType']=each.xpath('./td[2]/text()').extract()[0]
            item['peopleNum']=each.xpath('./td[3]/text()').extract()[0]
            item['workLocation']=each.xpath('./td[4]/text()').extract()[0]
            item['publishTime']=each.xpath('./td[5]/text()').extract()[0]
            
            #item will be sent to pipelines
            yield item

        # after handling one page,then launching another request
        if self.offset<3000:
            self.offset+=10
        else:
            raise "program ends"
        # request will be sent to scheduler
        yield scrapy.Request(self.url+str(self.offset)+'#a',callback=self.parse)
            
            
