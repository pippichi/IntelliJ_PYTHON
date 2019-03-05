# -*- coding: utf-8 -*-
import scrapy
import requests
import re
from scrapy import Request

class LagouSpider(scrapy.Spider):
    name = 'lagou'
    allowed_domains = ['www.lagou.com']
    start_url = 'http://www.lagou.com/'
    def start_requests(self):
        targets = ['Java', 'C++', 'shujuwajue', 'go', 'Android', 'iOS', 'JavaScript', 'jiqixuexi', 'tuxiangchuli', 'shenduxuexi', 'tuxiangshibie', 'yuyinshibie', 'jiqishijue', 'suanfagongchengshi', 'ziranyuyanchuli']
        for target in targets:
            url = '{start_url}/zhaopin/{target}/1/?filterOption=3/'.format(start_url=self.start_url,target=target)
            yield Request(url,callback=self.parse_index)
    def parse_index(self,response):
        nums = response.xpath(".//ul[@class='order']//li//div[@class='item page']//div//span[class='span totalNum']//text()")
        yield nums