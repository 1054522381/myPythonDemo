# !/usr/bin/python3
# -*- coding: utf-8 -*-
import sys
import getopt
import argparse
"""
1.sys.argv
2.getopt
3.argparse
"""


def sys_argv():
    """
    sys.argv，从外部获取输入的参数，返回的是一个列表list， 第一个参数是脚本的名字， 后面的是依次输入的参数，适合一些简单参数输入的情形。
    比如：
    命令行运行：python 26_脚本传参.py 123 789 aaa bb
    运行结果：['26_脚本传参.py', '123', '789', 'aaa', 'bb']
    """
    print(f'sys.argv=>{sys.argv}')


def my_getopt():
    """
    getopt模块，专门用来处理命令行参数，太复杂了，以后有需要再看
    """


def test_argparse():
    """
    argparse模块，用来解析命令行选项
    步骤：
    import argparse
    1.创建 parser
    2.add_argument
    3.parse_args
    """
    parser = argparse.ArgumentParser('description=Show the usage')
    # 运行：python 26_脚本传参.py 2020-01-01 结果：{'date_param': '2020-01-01'}
    # 如果命令行不带位置参数，会报required
    # parser.add_argument('date_param', type=str)

    # nargs：设置每个变量在命令行读入的值的数目，?：一个（默认），*：大于等于0个，列表，+：大于等于1个，argparse.REMAINDER：把命令行所有剩余的值都收集起来
    # 运行：python 26_脚本传参.py 2020-01-01 结果：{'date_param': '2020-01-01'}
    # 如果命令行不带参数，返回：{'date_param': '用默认值'}
    # parser.add_argument('date_param', nargs='?', default='用默认值')

    # 运行：python 26_脚本传参.py -d 2020-01-01 结果：{'date_param': '2020-01-01'}
    # 如果命令行不带参数，返回：{'date_param': '用默认值'}
    # 假如设置了required=True，default将失效
    parser.add_argument('-d', '--date_param', type=str, default='用默认值')
    args = parser.parse_args()
    print(f'argparse dict=>{args.__dict__}')


if __name__ == '__main__':
    sys_argv()
    test_argparse()
