from numpy import *

a = arange(4).reshape(2,2)
b = arange(4,0,-1).reshape(2,2)
print(b)
print(a+1,type(a))
print(array(a),type(array(a)))

for i in range(len(shape(a))):
    print(min(a[:,i]))
    print(a[i,:])

print(inf)#无穷

a = mat([[1,2],
         [3,5]])
b = a.flatten().A1
c = a.copy()
flatten = lambda x:[y for l in x for y in flatten(l)] if type(x) is list else [x]
d = flatten(a)
print(d)
print(c is a)
print(b)
print(ndim(b))


