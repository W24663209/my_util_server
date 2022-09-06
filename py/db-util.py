#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   db-util.py    
@Description TODO 数据库连接工具
@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/8/3 18:59:17   weizongtang      1.0         None
'''

# import lib
import json

import pymysql
import re

# conn = pymysql.connect(host=“你的数据库地址”, user=“用户名”,password=“密码”,database=“数据库名”,charset=“utf8”)
db = 'credit'
con = pymysql.connect(host='192.168.10.200', user='root', password='1234567', database=db, charset='utf8')
cur = con.cursor()


def create_entity(sql):
    cur.execute(sql)
    columns = cur.fetchall()
    entity_name = None
    entity_import_packages = []

    with open('../template/column.json', 'r') as f:
        column_types = json.loads(f.read())  # type: dict
    for column in columns:
        type = re.sub('\(.*\)', '', column[2]).upper()
        if column_types.keys().__contains__(type):
            print(column[0], column[1], column[2], column[3], column_types.get(type))


if __name__ == '__main__':
    create_entity(
        "select TABLE_NAME,COLUMN_NAME,COLUMN_TYPE,COLUMN_COMMENT from information_schema.COLUMNS where TABLE_NAME='t_user_info'")
