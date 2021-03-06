# -*- coding:utf-8 -*-
'''
    1、区分大小写
    2、python根据缩进来判断代码行与前一个代码行的关系（替代花括号和分号），所以不要轻易使用空格和缩进
'''

'''
一、数据类型（isinstance、type函数获取）
    
    A、数值（int、float）
        1、整数int、浮点数float。注意：如果对整数做除法运算，结果会返回一个整数（截除小数部分，也不会四舍五入）
        n、各种方法
            str(23)：将数值类型23转换成字符串类型23。例：'hi'+str(23)+'th'

    B、bool
        1、True、False（0、空字符串、空list等）
        2、逻辑运算符：and（且）、or（或）、not（非）
    
    C、None：不存在的

    # 下列都是集合数据类型
    D、str（字符串）
        1、字符串可以使用单引号或双引号
        2、字符串中可使用\t表示制表符，\n表示换行符
        n、各种方法：
            msg.title()：每个单词首字母转换成大写
            msg.upper()：每个字母转换成大写
            msg.lower()：每个字母转换成小写
            msg1 + msg2：字符串拼接
            msg.strip()：删除首尾空白。'h'和'h '并不相等
            msg.rstrip()：删除右空白
            msg.lstrip()：删除左空白
            msg[0:3:1]：切片，字符串截取

    E、list（列表，可以理解为数组）
        1、列表成员可以是任何数据类型
        n、各种方法：
            列表操作：
                vips.sort(reverse=True)：将vips成员按照一定规则（首字母、数值等）倒序排列（修改vips内部结构），没有reverse参数时正序排列。
                vips.reverse()：将vips成员倒序排列（修改vips内部结构）
                sorted(vips)：将vips成员正序排列（不会修改vips内部结构，相当于操作其副本）
                len(vips)：计算vips列表长度
                list(range(1,11,2))：range函数返回的偶数，list函数将每个返回值作为成员，组成一个数值列表并将其返回

            列表解析（list comprehensions）：
                squares = [val**2 for val in range(1,6)]：生成一个 由1（起始）到6（终止）之间每个数的平方 组成的数值列表
                等同于下面代码功能：
                    squares = []
                    for val in range(1,6):
                        squares.append(val**2)

            添加成员：
                vips.append(value)：将value添加到vips列表尾部
                vips.insert(index,value)：在vips列表index索引处添加成员value

            删除成员：
                vips.remove(value)：根据value值，删除匹配到的第一个成员，没有返回值
                del vips[index]：删除vips列表index索引处成员，没有返回值
                vips.pop(index)：删除vips列表index索引处成员，并将其作为返回值。index为负数，表示倒数第几个成员。
                                （如果没有index参数，删除的是列表最后一个成员）

            获取成员：
                切片

    F、tuple（元组）
        1、不能修改成员引用值的list称为 元组，所以它也是list的一种
        2、可以获取成员值
            切片

    G、dict（字典，可以理解为对象）
        1、key必须是不可变对象（基本数据类型），且不支持相同的键值对（后写入的key的value会覆盖前面相同的key的value）
        2、和list比较，dict有以下几个特点：
            查找和插入的速度极快，不会随着key的增加而变慢；
            需要占用大量的内存，内存浪费多。
        而list相反：
            查找和插入的时间随着元素的增加而增加；
            占用空间小，浪费内存很少。
        n、各种方法：
            删除成员
                d.pop(key)
            获取成员的value值
                d.get(key)
            获取dict所有成员的value值（返回 成员值 组成的list）(for in通过检索key的方式更节省内存，因为不需要生成list再检索)
                d.values()
            获取dict所有成员（返回 成员键值元组 组成的list）
                d.items()

    H、set
        1、接受一个Iterable类型的参数，返回一个无序的dict（自动删除相同的成员）
        n、各种方法：
            添加成员
                s.add(value)
            删除成员
                s.remove(value)

二、流程控制语句
    A、条件判断
        if 表达式:
            语句块
        elif 表达式:
            语句块
        else:
            语句块

    B、循环
        1、for vip in vips：遍历
        2、while循环

三、函数（先声明后调用）
    A、定义函数
        def fnName(args):
            函数体
        当函数体仅有一条语句pass时，函数没有任何功能，相当于一个占位符

    B、函数参数
        参数可使用5种参数（如果同时使用，一定按照下列顺序），分别是：
        必选参数：fnName(arg)
                    必不可少的参数
        默认参数（默认参数最好使用不变对象，否则会出现意想不到的逻辑错误）：fnName(arg1,arg2=value)
                    当只传入一个参数时，第二个参数默认使用value值
        可变参数：fnName(arg1,*arg2)
                    当传入参数个数超过一个时，超过的参数在函数体内封装成一个tuple，由可变参数arg2接收
        命名关键字参数（可使用默认值，避免调用时没有传命名关键字参数而报错）：fnName(arg1,*,arg3)或fnName(arg1,*arg2,arg3)
                        对关键字参数做出限制。如果一定要传入关键字参数，参数名一定要是arg3
        关键字参数：fnName(arg1,**arg2)
                        可传入任意多个含有参数名的参数(键值对))，在函数体内封装成一个dict，由关键字参数arg2接收

四、高阶特性
    A、切片
        1、operationObj[start:end:step]：
            从operationObj的start（省略时值为0）索引处开始，
            每跳过step个成员截取，
            一直截取到end（省略时值为operationObj的长度）索引处结束
        2、用途：
            字符串截取、list截取、tuple截取

    B、迭代for in（遍历）
        1、操作对象必须是一个可迭代对象（集合数据对象和生成器）
        2、判断操作对象的可迭代性：
            from collections.abc import Iterable
            isinstance(operationObj,Iterable)

    C、列表解析（list comprehensions）

    D、Generator（生成器）
        1、可遍历对象，类似JS的Generator
        2、生成方法：
            一、将生成list方式的中括号改成小括号g = (x*x for x in range(10))
            二、yield

五、模块和作用域
    A、模块
        1、为防止模块过多导致模块名冲突，可将模块打包。
        2、导入模块时，解释器的搜索路径：当前目录->已安装的内置模块->第三方模块，如果没有所以到将报错
        3、搜索路径信息存放在sys.path中，因此如果需要改变搜索方向，可以直接修改此变量（程序结束后失效），或者修改系统环境变量
    B、作用域
        1、此语言本身没有公共变量和私有变量关键词，因此官方约定一种写法：
            公共变量：vari
            私有变量：_vari 或 __vari
            内置变量：__name__、__doc__等

六、类
    A、定义
        1、class Student(object):           # 类名首字母大写，Student继承object类
            counter = 0                     # 定义类的属性（会被子类继承）
            def __init__(self,name,*,age):  # 初始化，self代表 类的实例，定义的时候不可省略且必须是作为第一个参数
                self.__name = name          # 初始化实例的私有变量
                self.__age = age            # 解释器会在内部将私有变量重新命名，例如_Student__name，所以其实在外部还是可以访问的（不建议外部访问）
    B、继承和多态
    C、静态语言 vs 动态语言（见runTwice(Camel())）
        对于静态语言（例如Java）来说，如果需要传入Animal类型，则传入的对象必须是Animal类型或者它的子类，否则，将无法调用run()方法。
        对于Python这样的动态语言来说，则不一定需要传入Animal类型。我们只需要保证传入的对象有一个run()方法就可以了
        这就是动态语言的“鸭子类型”，它并不要求严格的继承体系，一个对象只要“看起来像鸭子，走起路来像鸭子”，那它就可以被看做是鸭子。
    D、多重继承（MixIn混入）
        1、class Dog(Animal,Mammal):
            pass

七、I/O（I/O接口都是操作系统提供的，语言只是对其进行封装）
    A、文件数据操作
    B、内存操作
        1、StringIO ： 普通数据读取
        2、BytesIO : 二进制数据读取
    C、文件目录操作

八、进程、线程
    A、线程是最小的执行单元，而进程由至少一个线程组成。
        如何调度进程和线程，完全由操作系统决定，程序自己不能决定什么时候执行，执行多久

'''
# str示例
# msg = 'hello world'
# print(msg)
# msg = "msg has been changed"
# print(msg)


# list示例
# vips = ['zhao',8,'sun','li']
# print(vips.pop(-1))   # li


# tuple示例
# dimensions = (200,[100],43)
# dimensions[0] = 50    # 报错
# dimensions[1][0] = 50
# print(dimensions)       # (200,[50],43)


# dict示例
# d = {'wang':25,'li':42,'qian':23}
# d['qian'] = 00
# print(d.get('li'))      # 42
# print(d.pop('li'),d)    # 42 {'wang':25,'qian':00}
# print(d.values())       # dict_values([25, 42, 23])
# print(d.items())        # dict_items([('wang', 25), ('li', 42), ('qian', 23)])


# set示例
# s = set([1,4,3,1,3])
# s2 = set('zhao')
# print(s)    # {1,3,4}
# print(s2)    # {'h', 'z', 'a', 'o'}


# 流程控制语句示例
# inp = input('please inputer a number：')
# inp = int(inp)  # 即使用户输入的是数值，接收到的还是字符串数据类型
# if inp<=0:
#     print('请输入一个自然数')
#     inp = input('please inputer a number: ')
# elif inp==1:
#     print('请输入一个大于1的自然数')
#     inp = input('please inputer a number: ')
# else:
#     print(inp)


# 函数示例
# def person(name,age=18,*job,sex=None,nation=None,**gf):
#     print('name: ',name,'\nage; ',age,'\njob: ',job,'\nsex: ',sex,'\nnation: ',nation,'\ngf: ',gf)
# person('7seven',213,'dashu',gf='linux')
# name:  7seven
# age;  213
# job:  ('dashu',)
# sex:  None
# nation:  None
# gf:  {'gf': 'linux'}


# 切片示例
# strings = 'hello world'
# lists = list(range(50))
# tuples = (12,43,12,21)
# print(strings[:len(strings)-3:2],'\n',lists[::2],'\n',tuples[::1])


# 迭代示例
# from collections.abc import Iterable
# strings = '7seven'
# lists = [12,3,21,4,3]
# tuples = (21,'hehe',232)
# dicts = {'name':'7seven','age':23,'sex':'man'}
# sets = set(strings)
# # 上述都是可迭代对象
# # print(isinstance(strings,Iterable))
# # print(isinstance(lists,Iterable))
# # print(isinstance(tuples,Iterable))
# # print(isinstance(dicts,Iterable))
# # print(isinstance(sets,Iterable))
# for k,v in dicts.items():
#     print(k,v)


# 列表解析
# print([m+n for m in 'ABCD' for n in 'abcd'])
# ['Aa', 'Ab', 'Ac', 'Ad', 'Ba', 'Bb', 'Bc', 'Bd', 'Ca', 'Cb', 'Cc', 'Cd', 'Da', 'Db', 'Dc', 'Dd']
# print([i for i in set([12,23,32,12,34,21,32]) if i%2==0])
# [32, 34, 12]


# 生成器
# 斐波拉契数列1 1 2 3 5 8 13 21 ...
# def fib(num=5):
#     counter,prev,result = 0,0,1
#     while counter < num:
#         yield result
#         # t = (result,result+prev)
#         # prev = t[0]
#         # result = t[1]
#         prev,result = result,result + prev
#         # 不同于下述赋值
#         # prev = result
#         # result = result + prev

#         counter = counter + 1
#     return 'done'

# # 1 1 2 3 5 没有返回done
# # for x in fib():
# #     print(x)

# # 1 1 2 3 5 done
# g = fib()
# while True:
#     try:
#         print(next(g))
#     except StopIteration as e:
#         print(e.value)
#         break

# 凡是可作用于for循环的对象都是Iterable类型；
# 凡是可作用于next()函数的对象都是Iterator类型，它们表示一个惰性计算的序列；
# 集合数据类型如list、dict、str等是Iterable但不是Iterator，不过可以通过iter()函数获得一个Iterator对象。

# Python的for循环本质上就是通过不断调用next()函数实现的，例如：
# for x in [1, 2, 3, 4, 5]:
#     pass

# 实际上完全等价于：

# it = iter([1, 2, 3, 4, 5])
# while True:
#     try:
#         x = next(it)
#     except StopIteration:   # 捕获到StopIteration异常就退出循环
#         break


# 类的定义
# class Student(object):
#     def __init__(self,name,age):
#         self.__name = name
#         self.__age = age

# tom = Student('tom',23)
# print(tom._Student__name)

# 类的继承和多态
# class Animal(object):
#     def run(self):
#         print('Animal is running...')

# class Dog(Animal):
#     def run(self):
#         print('Dog is running...')

# class Cat(Animal):
#     def run(self):
#         print('Cat in running...')

# class Camel(object):        # 注意：Camel继承object，而不是Animal
#     def run(self):          # 注意：Camel继承object，而不是Animal
#         print('Camel is running...')

# def runTwice(Animal):       #调用的时候，只要实参已经定义了run方法，即使不是Animal类型，也是可以正常运行
#     Animal.run()
#     Animal.run()

# d = Dog()
# d.run()

# c = Cat()
# c.run()

# # print(isinstance(d,Animal))     # True
# # print(isinstance(d,Dog))        # True

# runTwice(Cat())                 # Cat in running...
# runTwice(Camel())               # 注意：Camel继承object，而不是Animal，但是还是正常运行，并打印Camel is running...


#I/O
#文件数据操作
# a : appdend 追加写入，不会覆盖原数据
# c : create 
# r : read
# w : write   会覆盖原数据
# rb : 读二进制数据
# wb : 写二进制数据
# encoding='gbk'  设置读写时字符编码（默认utf-8）
# errors='ignore'   忽略编码错误

# file = 'e:/github/2018/test.txt'
# file = 'e:/github/2018/images/set.png'

# with open(file,'rb') as f:
#     print(f.read())
# 等价于下面：
# try:
#     f = open(file,'rb')
#     print(f.readline())
# finally:
#     f.close()

# with open(file,'a') as f:
#     f.write('python i/o test\n')

# 内存操作
# from io import StringIO
# f = StringIO()
# f.write('hello')
# print(f.getvalue())     # hello

# 文件目录操作
# import os
# print(os.environ)       # 获取环境变量
# print(os.environ.get('path'))     # 获取环境变量具体值
# curdir = os.path.abspath('.')     # 获取当前文件的绝对路径
# testdir = os.path.join(curdir,'testdir')    # 路径拼合（不要直接拼合，不同平台路径分隔符不一样）
# os.mkdir(testdir)
# os.rmdir(testdir)

# os.listdir('.')   # 获取当前目录下的子文件和子目录
# 获取当前目录下的所有py后缀的子文件
# filelist = [x for x in os.listdir('/') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py']

#
#
#
#       如何查找e盘里的指定后缀文件
#
#
#

import os
import sys
sys.setrecursionlimit(2000)
def search(x,ext):
    if os.path.isfile(x) and os.path.splitext(x)[1]==ext:
        return True
    else:
        search(x,ext)

filelist = []
ext = '.py'
curdir = os.listdir('.')
for x in curdir:
    if search(x,ext):
        filelist.append(x)
print(filelist)