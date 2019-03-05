# -*- coding: utf-8 -*-
from scrapy import Spider,FormRequest

import requests
import re

from ..items import UserItem


class PyimagesearchSpider(Spider):
    name = 'pyimagesearch'
    allowed_domains = ['www.pyimagesearch.com']
    start_url = 'http://www.pyimagesearch.com/'
    max_page = 0
    pattern_num = re.compile('<div class="pagination.*?<a.*?<a.*?>([\d]+)</a>', re.S)

    def start_requests(self):
        response = requests.get(self.start_url)
        doc = response.text
        result = re.findall(self.pattern_num, doc)
        self.max_page = int(result[0])
        for page in range(self.max_page):
            data = {
                'mp':str(self.max_page),
                'page':str(page),
            }
            url = '{url}page/{page}/'.format(url=self.start_url,page=page+1)
            yield FormRequest(url,callback=self.parse_index,formdata=data)

    def parse_index(self, response):
        initials = response.xpath('.//article')

        for initial in initials:
            link = initial.xpath('.//header//h2[@class="title"]//a//@href').extract_first()
            name = initial.xpath('.//header//h2[@class="title"]//a//text()').extract_first()
            desc = initial.xpath('.//section[@class="entry"]//p//text()').extract_first()
            comment_num = initial.xpath('.//div//span[@class="post-comments comments"]//a//text()').extract_first()
            item = UserItem()
            item['names'] = name
            item['links'] = link
            item['descs'] = desc
            item['comment_nums'] = int(comment_num)
            yield item

        # for i in range(len(links)):
        #     print(names[i]+"        "+links[i]+"\n"+descs[i]+"\n"+common_nums[i]+"\n\n\n")
