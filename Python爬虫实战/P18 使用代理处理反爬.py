import requests
from urllib.parse import urlencode
from lxml.etree import XMLSyntaxError
from requests.exceptions import ConnectionError
from pyquery import PyQuery as pq
import pymongo
from Python爬虫实战.P18Mongo import *

client = pymongo.MongoClient('localhost')
db = client['weixin']

headers = {
    'Cookie': 'CXID=F470FEDC66D84E48845AD13130FA9B39; SUID=45EDE97A3965860A5A476E52000981A2; SUV=007E539673C11CF85B7BFB60B5B43044; wuid=AAGBzfWtIgAAAAqLEm/bHg4AGwY=; ad=$kllllllll2byPlClllllVmsKpcllllltloqyZllll9lllll4qxlw@@@@@@@@@@@; IPLOC=CN3301; ABTEST=7|1538661464|v1; SNUID=1A4B46FC8E8AF9E8058821B68FB51545; weixinIndexVisited=1; sct=1; JSESSIONID=aaaJM6jyK82gL4ndS9Wyw',
    'Host': 'weixin.sogou.com',
    'Referer': 'https://weixin.sogou.com/',
    'Upgrade-Insecure-Requests': 1,
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36'
}

proxy = None

def get_proxy():
    try:
        response = requests.get(PROXY_POOL_URL)
        if response.status_code == 200:
            return response.text
    except ConnectionError:
        return None

def get_html(url,count=1):
    print('Crawing',url)
    print('Trying Count',count)
    global proxy
    if count >= MAX_COUNT:
        print('Tried Too Many Counts')
        return None
    try:
        if proxy:
            proxies = {
                'http':'http://' + proxy
            }
            response = requests.get(url,allow_redirects=False,headers=headers,proxies=proxies) #由于requests自动处理302，因此调用allow_redirects=False
        else:
            response = requests.get(url,allow_redirects=False,headers=headers) #由于requests自动处理302，因此调用allow_redirects=False
        if response.status_code == 200:
            return response.text
        if response.status_code == 302:
            # Need Proxy
            print('302')
            proxy = get_proxy()
            if proxy:
                print('Using proxy',proxy)
                return get_html(url)
            else:
                print('Get Proxy Failed')
                return None
    except ConnectionError as e:
        print('Error Occurred',e.args)
        proxy = get_proxy()
        count += 1
        return get_html(url,count)

def get_index(KEYWORD,page):
    data = {
        'query':KEYWORD,
        'type':2,
        'page':page
    }
    queries = urlencode(data)
    url = BASE_URL + queries
    html = get_html(url)
    return html

def parse_index(html):
    doc = pq(html)
    items = doc('.news-box .news-list li .txt-box h3 a').items()
    for item in items:
        yield item.attr('href')

def get_detail(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        return None
    except ConnectionError:
        return None

def parse_detail(html):
    try:
        doc = pq(html)
        title = doc('.rich_media_title').text()
        content = doc('.rich_media_content').text()
        date = doc('#post-date').text()
        nickname = doc('#js_profile_qrcode > div > strong').text()
        wechat = doc('#js_profile_qrcode > div > p:nth-child(3) > span').text()
        return {
            'title':title,
            'content':content,
            'date':date,
            'nickname':nickname,
            'wechat':wechat
        }
    except XMLSyntaxError:
        return None

def save_to_mongo(data):
    if db['articles'].update({'title':data['title']},{'$set':data},True):
        print('Saved to Mongo',data['title'])
    else:
        print('Saved to Mongo Failed',data['title'])

def main():
    for page in range(1,101):
        html = get_index(KEYWORD,page)
        if html:
            article_urls = parse_index(html)
            for article_url in article_urls:
                article_html = get_detail(article_url)
                if article_html:
                    article_data = parse_detail(article_html)
                    print(article_data)
                    if article_data:
                        save_to_mongo(article_data)

if __name__ == '__main__':
    main()
