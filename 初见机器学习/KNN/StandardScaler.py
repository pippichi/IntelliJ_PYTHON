import numpy as np

class StandardScaler:

    def __init__(self):
        #不是用户传进来的参数，但是用户可能之后要用到，就在参数后面加_
        self.mean_ = None
        self.scale_ = None

    def fit(self,X):
        """根据训练数据集X获得数据的均值和方差"""
        assert X.ndim == 2

        self.mean_ = np.array([np.mean(X[:,i]) for i in range(X.shape[1])])
        self.scale_ = np.array([np.std(X[:,i]) for i in range(X.shape[1])])

        return self

    def transform(self,X):
        """将X根据这个StandardScaler进行均值方差归一化处理"""
        assert X.ndim == 2
        assert self.mean_ is not None and self.scale_ is not None
        assert X.shape[1] == len(self.mean_)

        resX = np.empty(shape=X.shape,dtype=float)
        for col in range(X.shape[1]):
            resX[:,col] = (X[:,col]-self.mean_[col]) / self.scale_[col]
        return resX

