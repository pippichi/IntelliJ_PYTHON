import jieba

from ReadFile import ReadCsv, cut2wd, get_feature_words, Count
import codecs
import pandas as pd
import numpy as np
def loan_csv(filename):
    # lists = []
    # with codecs.open(filename, 'r', 'utf-8') as f:
    #     for each in f.readlines():
    #         if each != '':
    #             lists.append(each.strip('\n'))
    Motion_result = ReadCsv(filename).data_np()
    lists = []
    for each in Motion_result[:, 1]:
        if each != ' ' and each != '':
            lists.append(each)
    return lists
#读取数据
Motion_result = ReadCsv("C:\\Users\\HASEE\\Desktop\\ai_challenger_sentiment_analysis_trainingset_20180816\\sentiment_analysis_trainingset1.csv").data_np()
Motion_validation = ReadCsv("C:\\Users\\HASEE\\Desktop\\ai_challenger_sentiment_analysis_validationset_20180816\\sentiment_analysis_validationset1.csv").data_np()




# pd.DataFrame(Motion_result[0:1000]).to_csv("C:\\Users\\HASEE\\Desktop\\ai_challenger_sentiment_analysis_trainingset_20180816\\sentiment_analysis_trainingset.csv",encoding="utf_8_sig")
# pd.DataFrame(Motion_validation[0:100]).to_csv("C:\\Users\\HASEE\\Desktop\\ai_challenger_sentiment_analysis_validationset_20180816\\sentiment_analysis_validationset.csv",encoding="utf_8_sig")
# df = pd.DataFrame(Motion_result)
# df.to_csv("C:\\Users\\HASEE\\Desktop\\ai_challenger_sentiment_analysis_trainingset_20180816\\sentiment_analysis_trainingset.csv")

# result = df.append(Motion_result).to_csv("C:\\Users\\HASEE\\Desktop\\ai_challenger_sentiment_analysis_trainingset_20180816\\sentiment_analysis_trainingset.csv")
# result2 = df2.append(Motion_validation).to_csv("C:\\Users\\HASEE\\Desktop\\ai_challenger_sentiment_analysis_trainingset_20180816\\sentiment_analysis_trainingset.csv")

# print(Motion_result.shape)
# print(Motion_validation.shape)
# lists = []
# for each in Motion_result[:, 1]:
#     if each!='':
#         lists.append(each.strip('\n'))
#
# y_train = Motion_result[:,2:]
# text = Motion_result[:,1]
# with codecs.open('corpus\\停用词表.txt', 'r', 'utf-8') as f:
#     list2 = []
#     for each in f.readlines():
#         if each != ' ' and each != '':
#             list2.append(each.strip('\n'))
# print(len(list2))
# print(text[0])
# list3 = jieba.cut(text[0],False)
# print(type(list3))
# for temp in list3:
#     print(type(temp))


# #存入text
# for t in text:
#     save_txt('txtfile.txt',t)

# print(readfile('txtfile.txt')[2])

# a = cut2wd(text)
#print(text[2])
# get_feature_words(text[3])
# b = Count(a)

