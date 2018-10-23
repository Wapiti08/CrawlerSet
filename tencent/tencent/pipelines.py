# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json

class ItcastPipeline(object):
    # optional,as a method of initializing a class
    def __init__(self):
        #create a folder
        self.filename=open("teacher.json",'wb')
    # must have, in order to process the item
    def process_item(self, item, spider):
        jsontext=json.dumps(dict(item),ensure_ascii=False)+'\n'
        self.filename.write(jsontext.encode("utf-8"))
        return item
    # optional, end method
    def close_spider(self,spider):
        self.filename.close()
