# -*- coding: utf-8 -*-

# Scrapy settings for taobao project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'taobao'

SPIDER_MODULES = ['taobao.spiders']
NEWSPIDER_MODULE = 'taobao.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'taobao (+http://www.yourdomain.com)'

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
    ':authority':' s.taobao.com',
    ':method':' GET',
    ':path':' /api?_ksTS=1539405217857_313&callback=jsonp314&ajax=true&m=customized&sourceId=tb.index&loc=%E5%8F%B0%E5%B7%9E&bcoffset=-3&commend=all&ssid=s5-e&search_type=item&q=%E5%8F%B0%E5%B7%9E&spm=a21bo.1000386.201856-taobao-item.1&s=36&imgfile=&initiative_id=tbindexz_20170306&ie=utf8&rn=3b2db146fd25e3569f64ddd6182a9e0b',
    ':scheme':' https',
    'accept':' text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01',
    'accept-encoding':' gzip, deflate, br',
    'accept-language':' zh-CN,zh;q=0.9',
    'cookie':' t=b2f843cf53372290d1257c2349582522; thw=cn; miid=954169008646012958; cna=OuvBE7fQ73kCAXAKFX65aOoz; hng=CN%7Czh-CN%7CCNY%7C156; tracknick=wili%5Cu5C0F%5Cu5CF0%5Cu5CF0sama; lgc=wili%5Cu5C0F%5Cu5CF0%5Cu5CF0sama; tg=0; enc=4zsq1mCsiwfVs8ywSI5Y6iocbazagKvZBCStGqlX6VHGqcf3g0bUcIZKv2PM%2F4w2Imq1mW0Hx0bVio%2BLyo%2Fhfg%3D%3D; x=e%3D1%26p%3D*%26s%3D0%26c%3D0%26f%3D0%26g%3D0%26t%3D0%26__ll%3D-1%26_ato%3D0; uc3=vt3=F8dByRqgM6LI437bE98%3D&id2=UUGjM7DammhAXQ%3D%3D&nk2=FPCuzQXcC2CtMiVlIAo%3D&lg2=U%2BGCWk%2F75gdr5Q%3D%3D; _cc_=VT5L2FSpdA%3D%3D; mt=ci=4_1&np=; _m_h5_tk=83e7bb90051f9e6de59194e28a3af934_1539412198526; _m_h5_tk_enc=2b8c9a366dc4c7e8ebe94959ba58b7fc; v=0; cookie2=7eb7c353ed7ebfc7ccc934f3aa4e802d; _tb_token_=feb3e5e1367d3; alitrackid=www.taobao.com; lastalitrackid=www.taobao.com; swfstore=175552; JSESSIONID=782227A50AE8F043B5ABE1B660296709; isg=BGNjV7MBPItUvfDB9IBNrFzd8qfN8PcezWe8MJXAv0I41IP2HSiH6kECyuT_9E-S',
    'referer':' https://s.taobao.com/search?q=%E5%8F%B0%E5%B7%9E&imgfile=&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.1000386.201856-taobao-item.1&ie=utf8&initiative_id=tbindexz_20170306&loc=%E5%8F%B0%E5%B7%9E',
    'user-agent':' Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36',
    'x-requested-with':' XMLHttpRequest',
}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'taobao.middlewares.TaobaoSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
   'taobao.middlewares.ProxyMiddleware': 543,
}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'taobao.pipelines.MongoPipeline': 300,
}

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

MONGO_URI = 'localhost'
MONGO_DB = 'taobaouser'
MONGO_TABLE = 'taobaouser'
PROXY_POOL = 'localhost:5000/get'
