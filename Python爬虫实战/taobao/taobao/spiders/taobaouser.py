# -*- coding: utf-8 -*-
import json
from ..items import TaobaoItem

from scrapy import Spider,FormRequest


class TaobaouserSpider(Spider):
    name = 'taobaouser'
    allowed_domains = ['www.taobao.com']

    search = '台州'
    start_url = 'https://s.taobao.com/search'
    max_page = 100

    def start_requests(self):

        url = '{url}?q={q}&loc={loc}'.format(url=self.start_url,q=self.search,loc=self.search)
        for page in range(self.max_page+1):
            data = {
                's':str(page*44)
            }
            yield FormRequest(url,formdata=data,callback=self.parse_detail,meta={'search':self.search})

    def parse_detail(self,response):
        taobaousers = response.xpath('//div[@id="attributes" and @class="attributes"]//ul')
        for taobaouser in taobaousers:
            print(taobaouser)
            try:
                name = taobaouser.xpath('//li[contains(text(),"厂名")]//text()').extract()
                detail_url = taobaouser.xpath('//li[@title="^1\d{10}"]//text()').extract()
                loc = taobaouser.xpath('//li[contains(text(),"厂址")]//text()').extract()
                taobaoitems = TaobaoItem()
                print(detail_url,name,loc)
                for field in taobaoitems.fields:
                    try:
                        taobaoitems[field] = eval(field)
                    except NameError:
                        self.logger.warning("Name is not defined:"+ field)
                yield taobaoitems
            except NameError:
                self.logger.warning('No responses')
