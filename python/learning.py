
'''
    1、区分大小写
    2、python根据缩进来判断代码行与前一个代码行的关系（替代花括号和分号），所以不要轻易使用空格和缩进
'''

'''
    A、数据类型--字符串

        1、字符串可以使用单引号或双引号
        2、字符串中可使用\t表示制表符，\n表示换行符
        n、各种方法：
                msg.title()：每个单词首字母转换成大写
                msg.upper()：每个字母转换成大写
                msg.lower()：每个字母转换成小写

                msg1+msg2：字符串拼接
                
                msg.strip()：删除首尾空白。'h'和'h '并不相等
                msg.rstrip()：删除右空白
                msg.lstrip()：删除左空白


    B、数据类型--数值

        1、整数int、浮点数float。注意：如果对整数做除法运算，结果会返回一个整数（截除小数部分，也不会四舍五入）
        n、各种方法
                str(23)：将数值类型23转换成字符串类型23。例：'hi'+str(23)+'th'


    C、列表（可以理解为数组）

        1、列表成员可以是任何数据类型
        2、各种方法：
                列表操作：
                    vips.sort(reverse=True)：将vips成员按照一定规则（首字母、数值等）倒序排列（修改vips内部结构），没有reverse参数时正序排列。
                    sorted(vips)：将vips成员正序排列（不会修改vips内部结构，相当于操作其副本）
                    vips.reverse()：将vips成员倒序排列（修改vips内部结构）
                    len(vips)：计算vips列表长度
                    list(range(1,11,2))：range函数返回1（起始）到11（终止）之间的偶数，list函数将每个返回值作为成员，组成一个数值列表并将其返回

                列表解析：
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
                    vips[start:end]：切片。获取vips列表从start索引处开始，到end索引处结束这中间的所有成员
                                    两个参数可以同时省略，此时表示 从起始处开始 切片 一直到末尾（复制一个副本）


    D、元组
        1、不能修改成员值的列表称为 元组
        2、可以获取成员值
'''
# 字符串示例
# msg = 'hello world'
# print(msg)
# msg = "msg has been changed"
# print(msg)

# 列表示例
# vips = ['zhao',8,'sun','li']
# print(vips.pop(-1))   # li

# 元组示例
# dimensions = (200,100)
# dimensions[0] = 50    # 报错