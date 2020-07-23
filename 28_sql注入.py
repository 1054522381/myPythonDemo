# -*- coding: utf-8 -*-
import pymysql
import sqlite3


def test_mysql(p: str):
    config = {'db': 'datasys', 'charset': 'utf8', 'host': 'localhost', 'user': 'root', 'passwd': '123456', 'port': 3306}
    con = pymysql.connect(**config)
    con.autocommit(1)
    cur = con.cursor()
    cur.execute('select 1, 2 from temp where id=' + p)
    result = cur.fetchall()
    print(list(result))
    cur.close()
    con.close()


def test_sqlite(p: str):
    con = sqlite3.connect("C:/Users/MeetYou/Desktop/my.db")
    cur = con.cursor()
    result = cur.executescript("select * from info where " + p)
    print(list(result))
    cur.close()
    con.close()


if __name__ == '__main__':
    test_mysql("1 union select database(),user()")
    test_sqlite("name='zhangsan'; delete from info;")
