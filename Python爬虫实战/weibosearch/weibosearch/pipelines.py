# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
import re
import time

from weibosearch.items import WeiboItem


class WeiboPipeline(object):

    def parse_time(self,datatime):
        if re.match('\d+月\d+日',datatime):
            datatime = time.strftime('%Y年',time.localtime()) + datatime
        if re.match('\d+分钟前',datatime):
            minute = re.match('(\d+)',datatime).group(1)
            datatime = time.strftime('%Y年%m月%d日 %H:%M',time.localtime(time.time()-float(minute)*60))
        if re.match('今天.*',datatime):
            datatime = re.match('今天(.*)').group(1).strip()
            datatime = time.strftime('%Y年%m月%d日',time.localtime()) + ' ' + datatime
        return datatime

    def process_item(self, item, spider):
        if isinstance(item,WeiboItem):
            if item.get('content'):
                item['content'] = item['content'].lstrip(':').strip()
            if item.get('posted_at'):
                item['posted_at'] = item['posted_at'].strip()
                item['posted_at'] = self.parse_time(item['posted_at'])

class MongoPipeline():
    def __init__(self,mongo_uri,mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db

    @classmethod
    def from_crawler(cls,crawler):
        return cls(
            mongo_uri=crawler.settings.get('MONGO_URI'),
            mongo_db=crawler.settings.get('MONGO_DB')
        )
    def open_spider(self,spider):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    def close_spider(self,spider):
        self.client.close()

    def process_item(self,item,spider):
        self.db[item.tabel_name].update({'id':item.get('id')},{'$set':dict(item)},True)
        return item