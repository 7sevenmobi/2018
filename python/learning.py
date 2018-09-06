# -*- coding:utf-8 -*-
'''
    1、区分大小写
    2、python根据缩进来判断代码行与前一个代码行的关系（替代花括号和分号），所以不要轻易使用空格和缩进
'''

'''
一、数据类型（type函数获取）
    A、str（字符串）
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

    B、数值（int、float）
        1、整数int、浮点数float。注意：如果对整数做除法运算，结果会返回一个整数（截除小数部分，也不会四舍五入）
        n、各种方法
            str(23)：将数值类型23转换成字符串类型23。例：'hi'+str(23)+'th'

    C、bool
        1、True、False（0、空字符串、空list等）
        2、逻辑运算符：and（且）、or（或）、not（非）

    D、None：不存在的

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
                        可传入任意多个含有参数名的参数，在函数体内封装成一个dict，由关键字参数arg2接收

四、高阶特性
    A、切片
        1、operationObj[start:end:step]：
            从operationObj的start（省略时值为0）索引处开始，
            每跳过step个成员截取，
            一直截取到end（省略时值为operationObj的长度）索引处结束
        2、用途：
            字符串截取、list截取、tuple截取

    B、迭代for in（遍历）
        1、操作对象必须是一个可迭代对象
        2、判断操作对象的可迭代性：
            from collections.abc import Iterable
            isinstance(operationObj,Iterable)

    C、列表解析（list comprehensions）

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
