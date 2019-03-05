# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html

import logging
import requests
import json

class CookiesMiddleware:

    def __init__(self,cookies_pool_url):
        self.logger = logging.getLogger(__name__)
        self.cookies_pool_url = cookies_pool_url

    def _get_random_cookies(self):
        try:
            response = requests.get('http://127.0.0.1/pyimagesearch/random')
            if response.status_code==200:
                return json.loads(response.text)
        except ConnectionError:
            return None

    @classmethod
    def from_crawler(cls,crawler):
        return cls(
            cookies_pool_url = crawler.settings.get('COOKIES_POOL_URL')
        )

    def process_request(self,request,spider):
        cookies = self._get_random_cookies()
        if cookies:
            request.cookies = cookies
            self.logger.debug('Using Cookies'+json.dumps(cookies))
        else:
            self.logger.debug('No Valid Cookies')