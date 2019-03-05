# import array
# arr = array.array('i',[i for i in range(100)]) #i 表示整型，f表示浮点型
# print(arr)

import numpy as np
arr = np.zeros((3,5))
print(help(np.random.normal()))

A = np.random.normal(1,3,(10,10))
print(A)
print(np.prod(A))

c = np.percentile(A,q = 50)  #np.percentile(A,p=?) 表示输出在数列A中?%位置的数
d = np.mean(A)
print(c)
print(d)

print(np.uint,"无符号整数")


