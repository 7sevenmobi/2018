#-*- coding:utf-8 -*-

'a test module'
# 解释器自动将第一行字符串注释成文档注释

__author__ = '7seven'

import sys

def greeting():
    args = sys.argv
    if len(args)==1:
        print('hello world')
    elif len(args)==2:
        print('hello %s' %args[1])
    else:
        print('too many arguments')

if __name__=='__main__':
    greeting()