from 尝试机器学习竞赛.ReadCsv import *
import re

#读取数据
Motion_result = ReadCsv("C:/Users/HASEE/Desktop/ai_challenger_sentiment_analysis_trainingset_20180816/sentiment_analysis_trainingset.csv").data_np()

#y_train

for i in range(5):
    text = Motion_result[:,1][i]

    size = 50
    rows = len(text) // size
    for j in range(rows+1):
        print(text[j*size:(j+1)*size])
    print("\n")







text = """第三次参加大众点评网霸王餐的活动。这家店给人整体感觉一般。首先环境只能算中等，其次霸王餐提供的菜品也不是很多，当然商家为了避免参加霸王餐吃不饱的现象，给每桌都提供了至少六份主食，我们那桌都提供了两份年糕，第一次吃火锅会在桌上有这么多的主食了。整体来说这家火锅店没有什么特别有特色的，不过每份菜品分量还是比较足的，这点要肯定！至于价格，因为没有看菜单不了解，不过我看大众有这家店的团购代金券，相当于7折，应该价位不会很高的！最后还是要感谢商家提供霸王餐，祝生意兴隆，财源广进"""
#
# words = ['环境','价位','菜品']
# words1 = ['不\w{0,10}高','不\w{0,10}多']
#
# for i in range(3):
#     word = words[i]+'.*?[，,！,。,；,？]'
#     test = re.findall(word,text)
#     if test:
#         for t in test:
#             for j in range(2):
#                 test1 = re.findall(words1[j],t)
#                 print(test1)