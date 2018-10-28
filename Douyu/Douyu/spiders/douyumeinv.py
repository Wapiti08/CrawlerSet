# -*- coding: utf-8 -*-
import scrapy
import json
from Douyu.items import DouyuItem

class DouyumeinvSpider(scrapy.Spider):
    name = 'douyumeinv'
    allowed_domains = ['capi.douyucdn.cn']
    offset=0
    url="http://capi.douyucdn.cn/api/v1/getVerticalRoom?limit=20&offset="

    start_urls=[url+str(offset)]

    def parse(self, response):
        #there are two parts in the text: one is error:0;
        # the other is data:{}
        data=json.loads(response.text)['data']
        for each in data:
            item=DouyuItem()
            item['nickname']=each['nickname']
            item['imagelink']=each['vertical_src']
            
            yield item
        self.offset+=20
        yield scrapy.Request(self.url+str(self.offest),callback=self.parse)