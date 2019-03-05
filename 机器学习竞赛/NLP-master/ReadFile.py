import jieba
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer,TfidfTransformer
import jieba.analyse
import xlrd
from collections import defaultdict

class ReadXls():

    def __init__(self,url,sheetNum):
        self.url = url
        self.sheetNum = sheetNum

    def _open_xls(self):
        xls_fl = xlrd.open_workbook(self.url)
        xls_sheets = xls_fl.sheets()[self.sheetNum-1]
        return xls_sheets

    #打开列
    def open_col(self,colNum=0):
        col_value = self._open_xls().col_values(colNum)
        return col_value

    #打开行
    def open_row(self,rowNum=0):
        row_value = self._open_xls().row_values(rowNum)
        return row_value

class ReadCsv():

    def __init__(self,url):
        self.url = url

    def _open_csv(self):
        df = pd.read_csv(self.url,encoding="utf-8")
        return df

    def data_np(self):
        df = np.array(self._open_csv())
        return df

def readfile(filename):
    fh = open(filename,'r',encoding='utf-8')
    data = []
    for x in fh.readlines():
        if (x.strip()!=''):
            data.append(x.strip())
    fh.close()
    return data

def readwords(filename):
    words = open(filename,'r',)

def save_txt(filename,text):
    with open(filename, 'w', encoding='utf-8') as f:
        for t in text:
            f.write(t)

#分词处理
def cut2wd(sentence):
    wdlist = jieba.cut(sentence)
    wdrst = []
    for w in wdlist:
        wdrst.append(w)
    stopwds = readfile('corpus\\停用词表.txt')
    newwd = []
    for w2 in wdrst:
        if w2 in stopwds or w2=='' or w2=='\n' or w2==' ':
            continue
        else:
            newwd.append(w2)
    return newwd

#筛选关键词
def get_feature_words(text):
    textrank = jieba.analyse.textrank
    keywords = textrank(text)
    for k in keywords:
        print(k+'/')

#统计词频
def Count(words):
    #转化成词频矩阵
    vectorizer = CountVectorizer()
    #转化成权值
    transformer = TfidfTransformer()
    word_freq = {}
    for word in words:
        if word in word_freq:
            word_freq[word]+=1
        else:
            word_freq[word]=1
    freq_word = []
    my_word = []
    for word,freq in word_freq.items():
        freq_word.append((word,freq))
        my_word.append(word)
    freq_word.sort(key=lambda x:x[1],reverse=True) #反序排列，根据第二个参数
    #max_number = 6      #int(input(u"需要前多少位高频词? "))
    print(freq_word)
    #词频矩阵
    X = vectorizer.fit_transform(my_word)
    #print(X)
    tfidf = transformer.fit_transform(X).toarray()
    #print(tfidf)
    feature_words = vectorizer.get_feature_names()
    new_feature_words = {}
    for i in range(len(tfidf)):
        for j in range(len(feature_words)):
            new_feature_words.update({str(feature_words[j]):int(tfidf[i][j])})
            print(i,j)
        print(new_feature_words)

def xlsIntoGoodTxt(words):
    with open('corpus\\褒义词表.txt', 'a', encoding='utf-8') as f:
        for w in words:
            if w == '':
                continue
            else:
                w = w + '\n'
                f.write(w)

def xlsIntoBadTxt(words):
    with open('corpus\\贬义词表.txt', 'a', encoding='utf-8') as f:
        for w in words:
            if w == '':
                continue
            else:
                w = w + '\n'
                f.write(w)

#情感定位
def pos(wddict):
    goodlist = readfile("corpus\\褒义词表.txt")
    gooddict = defaultdict()

    badlist = readfile("corpus\\贬义词表.txt")
    baddict = defaultdict()

    for word in wddict.keys():
        if word in goodlist and word not in badlist:
            gooddict[word] = wddict[word]*2
        elif word in badlist and word not in goodlist:
            baddict[word] = wddict[word]*-2



