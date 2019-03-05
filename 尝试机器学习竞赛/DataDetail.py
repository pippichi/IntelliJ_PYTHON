from 尝试机器学习竞赛.ReadCsv import *

#读取数据
Motion_result = ReadCsv("C:/Users/HASEE/Desktop/ai_challenger_sentiment_analysis_trainingset_20180816/sentiment_analysis_trainingset.csv").data_np()

#y_train
y_train = Motion_result[:,2:]

#查看类型
# print(type(Motion_result[:,1]))
for i in range(len(Motion_result[:,1])):
    text = Motion_result[:,1][i]
    WORDS = TextDeal().words(text)
    print(WORDS)