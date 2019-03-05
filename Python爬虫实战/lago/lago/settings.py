# -*- coding: utf-8 -*-

# Scrapy settings for lago project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'lago'

SPIDER_MODULES = ['lago.spiders']
NEWSPIDER_MODULE = 'lago.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'lago (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
    'Accept':' application/json, text/javascript, */*; q=0.01',
    'Accept-Encoding':' gzip, deflate, br',
    'Accept-Language':' zh-CN,zh;q=0.9',
    'Connection':' keep-alive',
    #'Cookie':' _ga=GA1.2.891432075.1543638988; user_trace_token=20181201123628-ab052d0f-f522-11e8-8ca7-5254005c3644; LGUID=20181201123628-ab053220-f522-11e8-8ca7-5254005c3644; index_location_city=%E6%9D%AD%E5%B7%9E; WEBTJ-ID=20181209145940-16791c3b1c7345-07af37b6db6896-b78173e-2073600-16791c3b1c83d0; X_HTTP_TOKEN=9650db08abf372b5482c0d1c20fd6f62; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2216791c43c2a666-029813227f7c9f-b78173e-2073600-16791c43c2b2a1%22%2C%22%24device_id%22%3A%2216791c43c2a666-029813227f7c9f-b78173e-2073600-16791c43c2b2a1%22%7D; sajssdk_2015_cross_new_user=1; LG_LOGIN_USER_ID=e955e2ab7a169ed22f9de5e33b0e9a4b185b520d08b8e9d3e8eee14fd5aaf1a1; _putrc=7489BBCF85202333123F89F2B170EADC; JSESSIONID=ABAAABAAAIAACBI968270AFBA6BC53E4E4AFBF7264352E8; login=true; unick=%E9%92%B1%E4%BE%9D%E5%B3%B0; showExpriedIndex=1; showExpriedCompanyHome=1; showExpriedMyPublish=1; hasDeliver=0; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1543638988,1544338780,1544343223; _gid=GA1.2.1409128404.1544343916; TG-TRACK-CODE=index_navigation; _gat=1; LGSID=20181209185921-7bbb7f45-fba1-11e8-8ec3-525400f775ce; PRE_UTM=; PRE_HOST=; PRE_SITE=https%3A%2F%2Fwww.lagou.com%2Fzhaopin%2FC%252B%252B%2F%3FlabelWords%3Dlabel; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2Fjobs%2F4429243.html; gate_login_token=aaad57468540242971c9355e528218153e70d9404f8f357f88e1f88ceb014d39; LGRID=20181209185924-7d7808bc-fba1-11e8-8ec3-525400f775ce; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1544353165; SEARCH_ID=5382495e25ca4bb7b6213c0edcd5d4fd',
    'Host':' www.lagou.com',
    'Referer':' https://www.lagou.com/zhaopin/C%2B%2B/?labelWords=label',
    'User-Agent':' Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36',
}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'lago.middlewares.LagoSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'lago.middlewares.LagoDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'lago.pipelines.LagoPipeline': 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
