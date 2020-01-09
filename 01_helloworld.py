#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Python 中的变量不需要声明。每个变量在使用前都必须赋值，变量赋值以后该变量才会被创建。
在 Python 中，变量就是变量，它没有类型，我们所说的"类型"是变量所指的内存中对象的类型。

Python3 中有六个标准的数据类型：
    Number（数字）包括 int、float、bool、complex（复数）。
    String（字符串）
    List（列表）
    Tuple（元组）
    Set（集合）
    Dictionary（字典）

"""

# 输入和输出
# name = input('please enter your name: ')
print('Hello,', 'World', sep=',,', end='###\n')
# print('Hello, %s' % name)

print('''line1
line2
line3''')

salary = 100.98100
print('salary:', salary)
print('salary: %.2f' % salary)

a = 'aa'
b = "aa"
print(a == b)
# 内存地址
print(id(a) == id(b))
