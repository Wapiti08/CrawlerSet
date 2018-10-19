# -*- coding: utf-8 -*-
import scrapy
from mySpider.items import ItcaseItem

class ItcastSpider(scrapy.Spider):
    #the name of spider
    name='itcast'
    #use the list often
    allowd_domains=['http://www.itcast.cn/']
    #the beginning url of spider
    start_urls=["http://www.itcast.cn/channel/teacher.shtml#"]
    
    def parse(self,response):
        # with open("teacher.html","wb") as f:
        #     f.write(response.body)
        #match the root note list collection of the teacher's name
        #via xpath
        teacher_list=response.xpath('//div[@class="li_txt"]')
        #use a set to store the items
        Teachers=[]
        for each in teacher_list:               
            #example a class
            item=ItcaseItem()
            # extract() can converse it into unicode 
            #name
            name=each.xpath('./h3/text()').extract()
            #title
            title=each.xpath('./h4/text()').extract()
	        #info
            info=each.xpath('./p/text()').extract()

            item['name']=name[0]
            item['title']=title[0]
            item['info']=info[0]
            
            #store the items into a set
            Teachers.append(item)
        return Teachers


        
