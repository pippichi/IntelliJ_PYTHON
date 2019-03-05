import numpy as np
from numpy.linalg import inv #inv是取矩阵的逆
from numpy import dot
from numpy import mat
import pandas as pd

dataSet = pd.read_csv('C:/Users/HASEE/Desktop/createData.csv')
# print(dataSet)

temp = dataSet.iloc[:,2:5]
temp['x0'] = 1
X = temp.iloc[:,[3,0,1,2]]
# print(X)
Y = dataSet.iloc[:,1].values.reshape(300,1)
# print(Y)
theta = dot(dot(inv(dot(X.T,X)),X.T),Y)
print(theta)

theta = np.array([1.,1.,1.,1.]).reshape(4,1)
alpha = 0.1
temp = theta
X0 = X.iloc[:,0].values.reshape(300,1)
X1 = X.iloc[:,1].values.reshape(300,1)
X2 = X.iloc[:,2].values.reshape(300,1)
X3 = X.iloc[:,3].values.reshape(300,1)

#同步更新theta
for i in range(20000):
    temp[0] = theta[0] - alpha*np.sum((dot(X,theta)-Y)*X0)/300.
    temp[1] = theta[1] - alpha*np.sum((dot(X,theta)-Y)*X1)/300.
    temp[2] = theta[2] - alpha*np.sum((dot(X,theta)-Y)*X2)/300.
    temp[3] = theta[3] - alpha*np.sum((dot(X,theta)-Y)*X3)/300.
    theta = temp

print(theta)












