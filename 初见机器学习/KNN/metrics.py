import numpy as np

def accuracy_score(y_true,y_predict):
    """计算y_true和y_predict之间的准确率"""
    assert y_true.shape[0] == y_predict.shape[0]

    return sum(y_true == y_predict)/len(y_true)