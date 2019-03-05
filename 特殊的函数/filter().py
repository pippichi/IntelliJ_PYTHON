def odd(x):
    return x % 2
temp = range(10)
show = filter(odd,temp)
print(list(show))

show2 = filter(lambda x:x%2,range(10))#filter过滤是指把为0（false）的数过滤
print(list(show2))

show3 = list(map(lambda x:x*2,range(10)))
print(show3)