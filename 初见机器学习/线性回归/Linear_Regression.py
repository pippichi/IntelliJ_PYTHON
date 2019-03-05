import numpy as np
from numpy.linalg import inv #inv是取矩阵的逆
from numpy import dot
from numpy import mat


# A = np.mat([[1,1]])
# B = np.array([1,1])
# print('A:\n',A,'\nB:\n',B)
#
# C = mat([[1,2],[2,3]])
# print('C:\n',C)
# print('C的逆:\n',inv(C))
#
# D = dot(A,C)
# print('\n',D)

#训练例子 y=2x
X = mat([1,2,3]).reshape(3,1)
Y = 2*X

#theta = (X'X)^-1X'Y
# theta = dot(dot(inv(dot(X.T,X)),X.T),Y)

#theta = theta - alpha * (theta*X-Y)*X
theta = 1.
alpha = 0.1
for i in range(100):
    theta = theta - np.sum(alpha*(dot(theta,X)-Y)*X.reshape(1,3))/3.
print(theta)








