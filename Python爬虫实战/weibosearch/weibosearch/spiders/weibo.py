# -*- coding: utf-8 -*-
import re
import tushare as ts

from scrapy import Spider,FormRequest,Request
from weibosearch.items import WeiboItem


class WeiboSpider(Spider):

    name = 'weibo'
    allowed_domains = ['weibo.cn']
    search_url = 'https://weibo.cn/search/mblog'
    max_page = 100

    def start_requests(self):
        result = ts.get_hs300s()
        keywords = result['code'].tolist()
        for keyword in keywords:
            # keyword = '000001'
            url = '{url}?keyword={keyword}'.format(url=self.search_url,keyword=keyword)
            for page in range(self.max_page+1):
                data = {
                    'mp':str(self.max_page),
                    'page':str(page)
                }
                yield FormRequest(url,self.parse_index,formdata=data,meta={'keyword':keyword})

    def parse_index(self, response):
        weibos = response.xpath('//div[@class="c" and contains(@id,"M_")]')
        print(weibos)
        for weibo in weibos:
            is_forward = bool(weibo.xpath('.//span[@class="cmt"]').extract_first())
            print(is_forward)
            if is_forward:
                detail_url = weibo.xpath('.//a[contains(.,"原文评论[")]//@href').extract_first()
            else:
                detail_url = weibo.xpath('.//a[contains(.,"评论[")]//@href').extract_first()
            print(detail_url)
            yield Request(detail_url,callback=self.parse_detail,meta={'keyword':response.meta['keyword']})

    def parse_detail(self,response):
        id = re.search('comment\/(.*?)\?',response.url).group(1)
        url = response.url
        # content = response.xpath('//div[@id="M_"]//span[@class="ctt"]//text()').extract_first()
        content = ''.join(response.xpath('//div[@id="M_"]//span[@class="ctt"]//text()').extract_first())
        print(id,url,content)
        comment_count = response.xpath('//span[@class="pms"]//text()').re_first('评论\[(.*?)\]')
        forward_count = response.xpath('//a[contains(.,"转发[")]//text()').re_first('转发\[(.*?)\]')
        like_count = response.xpath('//a[contains(.,"赞[")]//text()').re_first('赞\[(.*?)\]')
        print(comment_count,forward_count,like_count)
        posted_at = response.xpath('//div[@id="M_"]//span[@class="ct"]//text()').extract_first(default=None)
        user = response.xpath('//div[@id="M_"]//div[1]//a//text()').extract_first(default=None)
        print(posted_at,user)
        keyword = response.meta['keyword']
        weibo_item = WeiboItem()
        for field in weibo_item.fields:
            try:
                weibo_item[field] = eval(field)
            except NameError:
                self.logger.debug("Field is Not Defined: " + field)
        yield weibo_item