# -*- coding: utf-8 -*-
import scrapy


class HttpbinSpider(scrapy.Spider):
    name = 'httpbin'
    allowed_domains = ['httpbin.org']
    start_urls = ['http://httpbin.org/']

    def start_requests(self):
        yield scrapy.Request(url='http://httpbin.org/',method='POST',callback=self.parse_post)

    def parse(self, response):
        pass

    def parse_post(self,response):
        print('Hello',response.status,response.text)
