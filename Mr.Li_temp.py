# -*- coding: utf-8 -*-
"""
This is a temporary script file.
"""
import this#至理名言
print(this)
import math
x=2
y=3
print(math.pow(3,2))
print(round(3.4))
print(math.floor(18.1))
    
    
from math import ceil,floor
ceil(18.9)
floor(18.9)


name="yifeng Qian"
print(name.title())
print(name.upper())
print(name.lower())


feeling='I\'m so happy'
print(feeling)
feeling="\tI'm so happy"
print(feeling)
feeling="         I'm so happy   "
feeling=feeling.lstrip()
print(feeling.lstrip())
print(feeling)
feeling="           000000I'm so happy0000 "
feeling=feeling.strip(' 0')
print (feeling)
#2017年5月12日 14：33分

movies=["摔跤吧，爸爸",5,"银河护卫队",8,"亚瑟王",0.2,"喜欢你","春娇救志明",3]
movies.append("tidy beer")
print(movies[-1])
print(movies[9])
print(movies[-1].title())
for each in movies:
    print(each)
    for movie in movies:
        print(movie)
        

bikes=["ofo","xiaoming","HelloBike"]
print(bikes)
bikes.insert(0,"xiaolvche")
del bikes[0]
last_bike=bikes.pop()
print(last_bike)
bikes.remove("xiaoming")


cars=["bugatti",'30',"jaguar",'40',"maserati",'30',"benz"]
cars.sort()
print(cars)
sorted(cars)
cars.reverse()


cars=["bugatti",30,"jaguar",40,"maserati",30,"benz",50]
for car in cars:
    print(str(car)+"is my car")
    

for value in range(1,8):
    print(value**2)


numbers=list(range(1,100))
print(numbers)


numbers=list(range(1,11,2))
print(numbers)

numbers=list(range(2,11,2))
print(numbers)


squares=[]
for value in range(1,11):
    squares.append(value**2)
print(squares)
min(squares)
max(squares)
sum(squares)

squares=[]
squares = [value**2 for value in range(1,11)]
print(squares)

for value in range(1,11):
    square=[value**2]
    print(square)
    

players=["kuli","kebi","zhanmusi","lindan","heli"]
print(players[:])
NBAPlayers=players
print(NBAPlayers)   
players.append("迪士尼")
print(players)
print(NBAPlayers)


pi=(3.1415926535)   
dimensions=(200,50)
print(dimensions[0])
#遍历元组里的所有值        
for dimension in dimensions:
    print(dimension)
  
      
person_1={'name':'胡歌','birthday':1982,
          'profession':'演员',}        
drama1={'name':'琅琊榜','expisodes':54,
           'release_time':'2015-12-06',
           'type':'costume_piece',
           'summary':'17岁林殊率赤焰军出征',
           'actors':person_1}
print(drama1['name'])
person_2={'name':'吴磊','birthday':1999,
          'profession':'演员',}
stars=[person_1,person_2]
print(stars[0]['name'])
person_2['master_work']='琅琊榜'
del person_2['name']
print(person_2)
year=person_2['birthday']
name=person_2['name']
print (name+"的生日是:"+str(year))
    

favorite_laptop={'yao-jiaying':'surface','tang_xuexue':'dell',
                 'li_jintao':'asus','shen_sicong':'macbook',
                 'zhang_biqin':'lenovo','shi_jiadie':'dell',}
for key,value in set(favorite_laptop.items()):#set的无序用法
    if key=='li_jintao':
        print ("hahaha")
        continue
    print ("同学 "+key.title()+" 拥有 "+value+" 笔记本电脑 ")
print ("感谢上述同学参与配合调查！" ) 
    
name=input('input your name please: ')
print("我的名字是: "+name)


def greet(name):
    print ("hello"+" "+name+",nice to meet you!")
    return "哈哈，我已问候"
greet(name="jintao")
answer=greet("8k")
    

count_number=0
summarize=0
while count_number<=10:
    summarize+=count_number
    count_number+=1
print("从1加到10为:"+str(summarize))
    

playstring="!"
saygoodbye="quit"
message=saygoodbye+playstring
while message==('quit!'):
    print (saygoodbye)
    message=input(playstring)
    print (message)
    
active=True
while active:
    print (saygoodbye)
    message=input(playstring)
    if message=='quit':
        active=False
    else:
        print (message)
        
active=True
while active:
    message=input(playstring)
    if message=='quit':
        continue
    if message=='over':
        break
    print("我一直出现,直到over")   
        
active=True
while active:
    message=input(playstring)
    if message=='quit':
        active=False
    if message=='over':
        print (message)
    print("我一直出现,直到quit") 
    
    
def greet(name):
    print (name.title()+"您好,快下课了!")
    print("我!"+str(age)+"岁")
    return "好的,我马上交作业!"
answer=greet('zhaojiali')
greet(age=19,name='xiaoming')

def hello():
    print('hello python!')
    
def greet(names):
    for name in names:
        print (name.title()+"nihao"+"wandeyukuai") 
names=['xiaoming','xiaozhao','xiaoyuan']
greet(names) 


class Dog(object):
    def __init__(self,name,age):
             self.name=name
             self.age=age        
    def sit(self):
        print (self.name.title()+" is setting")       
    def roll_over(self): 
        print(square)
square="Yes!"
my_dog=Dog("8k",2)
my_dog.sit()
my_dog.roll_over()


players=["Owen","Durnt","Graim","Tomson"]
print(players[0:3])
print(players[1:])
print(players[-1:])
print(players[:1])


s = "hello world"
print (s[2:7])
print (s[5])
print (s[:2])
print (s[2:])
#注意左闭右开


list_a=["str",1,["a","b","c"],4]
list_b=["hello"]
print (list_a[2][1])
print (list_b * 2)
print (list_a + list_b)


dict_a = {
        "name":"Alan",
        "age":19,
        1:"level_1"
        
   }
print (dict_a[1])
print ("name" not in dict_a)#判断语句
print ("某某某" in dict_a)#判断语句
print (dict_a.keys())#‘：’前面的数据
print (dict_a.values())#‘：’后面的数据
print (dict_a.items())#包含一条“数据”+‘：’+”数据“


a=7
b=3
print (a // b)

#[0,10)
for i in range(0,10):
    print (i)

for a in range(1,5):
    print (a)
    if a == 3:
        break
   

list_a = [1,2,"test"]
for i in list_a:#这里的i是从1开始的！！！
    print (i)
    if i == 2:
        break
    print ("OK")

list_a = [1,2,"test"]
for i in list_a:#这里的i是从1开始的！！！
    print (i)
    if i == 2:
        continue
    print ("OK")

for a in range(1,10):
    print (a)
    if a == 5:
        continue
    print ("ok")



cars=["bmw",30,"Jaguar",40,"benz",30,"toyuta",30]
for car in cars:
    print(str(car)+" is my car")


ages=list(range(0,101)) 
a=ages
for age in a:
    if age<=3:
        print("不要钱")
    elif age>=65:
        print("100港币")
    else:
        print("500港币")    
        
#九九乘法表
for i in range(1,10):
    a=1
    while a<=i:
        print("{0}*{1}={2:0>2}".format(a,i,a*i),end='\t')
        a+=1
    print()


favorite_laptop={'yao_jiaying':'surface',
                 'tang_xuexue':'dell',
                 'li_jintao':'asus',
                 'shen_sicong':'macbook',
                 'zhang_biqin':'lenovo',
                 'shi_jiadie':'dell',}
for value in set(favorite_laptop.values()):
    print ("笔记本品牌 "+" "+value)
print( "有这几种品牌啊！")


name=set(['qyf','ljt','dyx','wjw','xfy'])
name.add('qyf')
print(name)


playString="welcome to play the game!\t"
sayGoodBye="play or quit?"
message=""
while message!="quit":
    print (sayGoodBye)
    message=input(playString)
    print (message)


guest_list=["xiaoming",'shenkuo',"jinjin",3]
guest_list =guest_list[:-(3-2)] 
print (guest_list)
for guest in guest_list:
    print ("尊敬的"+str(guest)+"请您前来赴宴！")
del guest_list[0:2]
print (guest_list)


list=[a]
for a in range(3,31):
    if a%3==0 :
        print(a)
        
list=[a];
for a in range(1,11):#左闭右开
    print (a**3)

#不知道要不要加进去的算法1
list1=[1,2,3,4,5,6,7,8,9,10]
list2=[]
for n in list1:
    list2.insert(n,n**3)
print(list2)

#列表解析式算法A
list1=[1,2,3,4,5,6,7,8,9,10]
list2=[n**3 for n in list1]
print (list2)

current_users=["xiaoming","huahua","daxiong","keke","lele"]
new_users=["xiaoming","huahua","dake","duck","james"]
for value in new_users:
    if value in current_users:
        print ("sorry,"+value+" "+"can not be used!")
    if value not in current_users:#注意可以用not in
        print (value+" "+"can be used!")


print("Please tell us your age")
ages=input("input your age please: ")
age=int(ages)#类型转换
if age<3:
    print("it's free of charge.")
elif age>=3 and age<=12:
    print("it takes 10 dollars")
else:
    print("it takes 15 dollars")


#difference 只有在字典中可以用，要先转化成字典
name_list=["xiaoming","xiaohong","xiaohuang","xiaohei","keke","xiaoli"]
favorite_languages={'xiaoming':'chinese',
                    'xiaohei':'japanese',
                    'xiaohuang':'deyu',
                    }
for key in favorite_languages:
    print (key +" "+ "thanks for joining!")
for value in (set(name_list).difference(favorite_languages)):
    print (value + " "+"please join the survey!")

#比较不同字典
favorite_languages={'xiaoming':'chinese',
                    'xiaohei':'japanese',
                    'xiaohuang':'deyu',
                    }
favorite_language={'xiaomin':'chinese',
                    'xiaohei':'japanese',
                    'xiaohuang':'deyu',
                    }
dif=set(favorite_language.items())^set(favorite_languages.items())
print(dif)


favorite_places={'xiaoming':'hangzhou''suzhou',
                 'xiaohua':'lanzhou''suzhou',
                 'yifeng':'chengdu''chongqin''nanjing',}
for key in favorite_places:
    print (key+" "+"likes"+" "+favorite_places[key]+" "+"most!")


sandwish_orders=["Cheese sandwish",
                 "xuancainiurou sandwish",
                 "France sandwish",
                 "Chinese sandwish",
                 "zhishihuotui sandwish",]
finished_sandwishes=[]
for value in sandwish_orders:   
        print ("I made your"+" "+value)
        finished_sandwishes.append(value)
for key in finished_sandwishes:
    print (key+" "+"has been maken!")
print (finished_sandwishes)


class Home(object):    
    def _init_make_sure(self,city,country):
        self.city=city
        self.country=country
        print("My home is in "+city+" "+country)
myHome=Home()
myHome._init_make_sure("Hangzhou","China")


(x,y)=(int(input("qingshurux: ")),int(input("qingshuruy: ")))
print (x*y)

int(3/2)
round(3.2/2)


def city_country(city,country):
    city_compose=city+","+country
    city_compose=city_compose.title()
    print (city_compose)
city_country('chengdu','china')


list1=['liuqian','dawei','kelisi','anjier'] 
list2=[]
def make_great():
    for a in list1:
        list2="the Great"+" "+str(a)
        print (list2)
def add_list2():
    for a in list1:
        list2.append("the Great"+" "+str(a))
    print(list2)
def show_magicians():
    for value in list2:
        value=value.title()      
        print (value)
make_great()
add_list2()
show_magicians()


def make_car(manufacturer,model,color,tow_package):
    car={"manufacturer":manufacturer,"model":model,
         "color":color,"tow_package":tow_package,}
    return car
Car=make_car('subaru','outback','blue',True)
print (Car)

    
class Resturant(object):
    def __init__(self,resturant_name,cuisine_type):
        self.resturant_name=resturant_name
        self.cuisine_type=cuisine_type
    def open_resturant(self): 
        print(self.resturant_name.title()+" is open!!")
    def describe_resturant(self):
        print (self.resturant_name+" "+"have"+" "+self.cuisine_type)
resturant=Resturant()
resturant.__init__("luxiaoman","hongshaorou")       
print (resturant.cuisine_type)
print (resturant.resturant_name)
resturant.describe_resturant()
resturant.open_resturant()


lists=[]
for list_number in range(20):
    new_list={'color':'red'}
    lists.append(new_list)
print (lists)


k="tell us your name!\n"
k += "what is your name?\n"
active = True
while active:
    m=input(k)
    if m=='quit':
        active = False
    else:
        continue
    
#------------------------------------------------------------------------------------------------------------------------------------------------
        
import numpy as np
array = np.array([[1,2,3],
                  [3,4,5],
                  [4,5,6]])
print(array)
print("number of dim: ",array.ndim)
print("shape:",array.shape)
print("size: ",array.size)

import numpy as np
array = np.array([[1,2,3],
                  [3,4,5],
                  [4,5,6]],dtype=np.float)
print(array.dtype)
print(array)

import numpy as np
a=np.zeros((3,4),dtype=np.int)
print(a)
b=np.ones((3,2),dtype=np.int)
print(b)
c=np.empty((3,3))
print(c)
d=np.arange(1,10).reshape((3,3))
print(d)
e=np.linspace(1,10,4,dtype=np.int).reshape((2,2))
print(e)

import numpy as np
a=np.array([[1,1,1],
           [2,2,2]])
b=np.arange(6).reshape((2,3))
c=a-b
print(a,"\n",b)
print(c)
c=10*np.sin(a)
print(c)
print(b<3)
print(b==3)

import numpy as np
a=np.array([[1,2],
            [2,3]])
b=np.arange(4).reshape((2,2))
c=a*b
print(c)
d_dot2=a.dot(b)
d_dot=np.dot(a,b)
print(d_dot2)

import numpy as np
a=np.random.random((3,3))
print(a)
print(np.sum(a))
print(np.max(a))
print(np.min(a))
print(np.max(a,axis=1))
print(np.max(a,axis=0))

import numpy as np 
A=np.arange(2,14).reshape((3,4))
print(np.argmax(A))#最大值索引
print(A.argmax())
print(np.mean(A))
print(A.mean())
print(np.average(A))
print(np.median(A))
print(np.cumsum(A).reshape((3,4)))#累加
print(np.diff(A))#前两个数的差
print(np.nonzero(A))#找出不是0的数,,,显示的是第几行第几列的数非零

import numpy as np
A=np.arange(14,2,-1).reshape((3,4))
print(np.sort(A))#逐行排序
print(np.transpose(A).dot(A))
print(A.T)
print(np.clip(A,5,9))
print(A[1][0])
print(A[1,0])
print(A[:,1])

import numpy as np
A=np.arange(2,14).reshape((3,4))
print(A)
print(A[1,1:3])
for raw in A:
    print(raw)
for column in A.T:
    print(column)
print(A.flatten())#与A.flat的区别在于它可以返回值，而A.flat是个迭代器，不return值
for item in A.flat:
    print(item)
    

import numpy as np
A=np.array([1,2,3])[:,np.newaxis]
B=np.array([2,3,4])[:,np.newaxis]
C=np.vstack((A,B))
C=np.hstack((A,B))
print(C)
print(B.reshape(3,1).shape)
print(A[:,np.newaxis])
print(A[np.newaxis,:].shape)
C=np.concatenate((A,B,A,B,B),axis=1)
C=np.concatenate((A,B,A,B,B),axis=0)
print(C)


import numpy as np
A=np.arange(12).reshape((3,4))
print(A)
print(np.split(A,2,axis=1))#axis表示对行进行操作，把行切成两半
print(np.array_split(A,2,axis=0))
print(np.vsplit(A,3))
print(np.hsplit(A,4))


import numpy as np
A=np.arange(12)
B=A
B is A
B[1:3]=[22,11]
C=A.copy()
C is A


import numpy as np
import pandas as pd
s=pd.Series([1,2,3,np.nan,44,1])
s
dates=pd.date_range('20180530',periods=6)
dates
df=pd.DataFrame(np.random.randn(),index=dates,columns=['a','b','c','d'])
df
df1=pd.DataFrame(np.arange(12).reshape((3,4)))
df1
df2=pd.DataFrame({'A':1.,
                  'B':pd.Timestamp('20180101'),
                  'C':pd.Series(1,index=range(4),dtype='float32'),
                  'D':np.array([3]*4,dtype='int32'),
                  'E':pd.Categorical(["test","train","test","train"]),
                  'F':'foo'})
df2
print(df2.dtypes)
df2.index
df2.columns
df2.values
df2.describe()
df2.T
df2.sort_index(axis=0,ascending=False)
df2.sort_values(by='E')

import numpy as np
import pandas as pd
dates=pd.date_range('20180101',periods=6)
df=pd.DataFrame(np.arange(24).reshape((6,4)),index=dates,columns=['A','B','C','D'])
df
df.A
df['A']
df[0:3]
df['20180101':'20180103']
print(df.loc['20180102'])
print(df.loc[:,['A','B']])
print(df.loc['20180102',['A','B']])
print(df.iloc[3:5,1:3])
print(df.ix[:3,['A','C']])
print(df[df.A>8])

#python3.7版本
#class创建
import attr

@attr.s(hash=True)
class Product():
    id = attr.ib()
    author_id = attr.ib()
    spu_id = attr.ib()
    title = attr.ib(repr=False,cmp=False,hash=False)
    item_id = attr.ib(repr=False,cmp=False,hash=False)
    n_comments = attr.ib(repr=False,cmp=False,hash=False)
    creation_time = attr.ib(repr=False,cmp=False,hash=False)
    update_time = attr.ib(repr=False,cmp=False,hash=False)
    source = attr.ib(default='',repr=False,cmp=False,hash=False)
    parent_id = attr.ib(default=0,repr=False,cmp=False,hash=False)
    ancestor_id = attr.ib(default=0,repr=False,cmp=False,hash=False)

p1 = Product(1, 100001, 2003, 20, 1002393002, '这是一个测试商品1', 2000001, 100, None, 1)
p2 = Product(1, 100001, 2003, 20, 1002393002, '这是一个测试商品2', 2000001, 100, None, 2)
p3 = Product(3, 100001, 2003, 20, 1002393002, '这是一个测试商品3', 2000001, 100, None, 3)
p1
p1 == p2
p1 > p3
{p1,p2,p3}
attr.asdict(p1)
attr.asdict(p1,filter=lambda a,v:a.name in ("id","title","author_id"))

#字段类型验证
#1、装饰器
@attr.s
class C():
    x = attr.ib()
    @x.validator
    def check(self,attribute,value):
        if value > 42:
            raise ValueError("x must be smaller or equal to 42")
C(42)
C(43)
#2、属性参数
def x_smaller_than_y(instance,attribute,value):
    if value >= instance.y:
        raise ValueError("'x' has to be smaller than 'y'!")
@attr.s
class C():
    x = attr.ib(validator=[attr.validators.instance_of(int),
                           x_smaller_than_y])
    y = attr.ib()
C(3,4)
C(4,3)

#属性类型转化
@attr.s
class C():
    x = attr.ib(converter=int)
o = C("1")
o.x

#包含元数据
@attr.s
class C():
    x = attr.ib(metadata={'My_metadata':1})
attr.fields(C).x.metadata
attr.fields(C).x.metadata['My_metadata']

#dataclasses模块
from dataclasses import dataclass,field
from datetime import datetime

@dataclass(unsafe_hash=True,order=True)
class Product():
    id:int
    author:int
    brand_id:int
    spu_id:int
    title:str=field(hash=False,repr=False,compare=False)
    item_id:int=field(hash=False,repr=False,compare=False)
    n_comments:int=field(hash=False,repr=False,compare=False)
    creation_time:datetime=field(default=None,repr=False,compare=False,hash=False)
    update_time:datetime=field(default=None,repr=False,compare=False,hash=False)
    source:str=field(default='',repr=False,compare=False,hash=False)
    parent_id:int=field(default=0,repr=False,compare=False,hash=False)
    ancestor_id:int=field(default=0,repr=False,compare=False,hash=False)

p1 = Product(1, 100001, 2003, 20, 1002393002, '这是一个测试商品1', 2000001, 100, None, 1)
p2 = Product(1, 100001, 2003, 20, 1002393002, '这是一个测试商品2', 2000001, 100, None, 2)
p3 = Product(3, 100001, 2003, 20, 1002393002, '这是一个测试商品3', 2000001, 100, None, 3)
p1

p1==p2
p1>p3
{p1,p2,p3}
from dataclasses import asdict
asdict(p1)
