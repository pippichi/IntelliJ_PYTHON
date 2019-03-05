import requests
import re

class selfTest:

    def __init__(self):
        self.__headers = {
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36'
        }
        self.__html = 'https://www.pyimagesearch.com/page/{offset}/'
        self.pattern = re.compile('<div.*?<article.*?<h2 class="title".*?<a href="(.*?)".*?>(.*?)</a>.*?<section.*?<p>(.*?)</p>.*?<div class="post-more".*?<a.*?<a.*?</i>(.*?)</a>',re.S)
        self.pattern_num = re.compile('<div class="pagination.*?<a.*?<a.*?>([\d]+)</a>',re.S)
        self.__num = self.total_num()

    def open(self,count=0):
        response = requests.get(self.__html.format(offset=count+1),headers=self.__headers)
        doc = response.text
        results = re.findall(self.pattern,doc)
        for res in results:
            url,title,desc,num = res
            print(title,"\n\n",url,"\n\n",desc,"\n\n评论数: ",num,"\n\n")
        if count < self.__num:
            self.open(count+1)

    def total_num(self):
        response = requests.get(self.__html.format(offset=1),headers=self.__headers)
        doc = response.text
        result = re.findall(self.pattern_num,doc)
        return int(result[0])

if __name__=='__main__':
    selfTest().open()