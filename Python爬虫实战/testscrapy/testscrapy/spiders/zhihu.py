# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class ZhihuSpider(CrawlSpider):
    name = 'zhihu'
    allowed_domains = ['www.zhihu.com']
    start_urls = ['http://www.zhihu.com/']

    custom_settings = {
        'DEFAULT_REQUEST_HEADERS' : {
            'User-Agent' : None,
            'Accept-Language': 'en',
        }
    }

    def __init__(self,mongo_uri,mongo_db,*args,**kwargs):
        super(ZhihuSpider,self).__init__(*args,**kwargs)
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri = crawler.settings.get('MONGO_URI'),
            mongo_db = crawler.settings.get('MONGO_DB')
        )
    def parse(self,response):
        pass

    rules = (
        Rule(LinkExtractor(allow=r'Items/'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        i = {}
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()
        return i
