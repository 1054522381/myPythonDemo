# !/usr/bin/python3
# -*- coding: utf-8 -*-
import os
import datetime


def test_file():
    # 获取文件绝对路径，返回包含文件名，如：D:\ideaProjects\my_script\handle\member_tapd_data.py
    print(os.path.abspath(__file__))
    # 获取文件所在目录，返回只有目录，如：D:/ideaProjects/my_script/handle
    print(os.path.dirname(__file__))


def test_time():
    # 昨天的日期 <class 'datetime.date'>
    yesterday = datetime.date.today() + datetime.timedelta(days=-1)
    yesterday_str = str(yesterday)

    # 指定日期加一天
    first_day = datetime.date(2019, 12, 24)
    first_day = first_day + datetime.timedelta(days=1)
    print(f"day=>{first_day}")


if __name__ == '__main__':
    test_time()

