import pandas as pd
import numpy as np
import re,collections
from 尝试机器学习竞赛.config import *


class ReadCsv():

    def __init__(self,url):
        self.url = url

    def _open_csv(self):
        df = pd.read_csv(self.url)
        return df

    def data_np(self):
        df = np.array(self._open_csv())
        return df

class TextDeal():

    def __init__(self):
        self.score = np.zeros((len(KEY_WORDS),1),dtype=int)

    # def train(self,features):
    #     model = collections.defaultdict(lambda :0) #0是默认值
    #     for f in features:
    #         model[f] += 1
    #     return model.items()


# 0--->交通
# 1--->服务态度
# 2--->上菜速度
# 3--->性价比
    def words(self,text):
        for i in range(len(KEY_WORDS)):
            word = KEY_WORDS[i] + '.*?[，,！,。,；,？]'
            test = re.findall(word, text)
            if test:
                for t in test:
                    for j in range(len(BAD_LEVELS)):
                        final_words = re.findall(BAD_LEVELS[j], t)
                        if final_words:
                            if i==0:
                                self.score[0] -= 1
                            elif i==1:
                                self.score[1] -= 1
                            elif i==2:
                                self.score[2] -= 1
                            elif i==3:
                                self.score[3] -= 1
                        if not final_words:
                            final_words = re.findall(GOOD_LEVELS[j],t)
                            if final_words:
                                if i == 0:
                                    self.score[0] += 1
                                elif i == 1:
                                    self.score[1] += 1
                                elif i == 2:
                                    self.score[2] += 1
                                elif i == 3:
                                    self.score[3] += 1
        return self.score