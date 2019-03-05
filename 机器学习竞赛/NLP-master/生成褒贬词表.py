import codecs

from ReadFile import ReadXls, xlsIntoGoodTxt,xlsIntoBadTxt

col_value = ReadXls('D:/迅雷下载/情感类词库/SentimentAnalysisWordsLib/褒贬词及其近义词/褒贬词及其近义词.xls',1).open_col()
xlsIntoGoodTxt(col_value)
xlsIntoBadTxt(col_value)
