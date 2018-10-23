# -*- coding: utf-8 -*-
import scrapy


class TencentcareersSpider(scrapy.Spider):
    name = 'tencentCareers'
    allowed_domains = ['tencent.com']
    start_urls = ['http://tencent.com/']

    def parse(self, response):
        pass
