#!/usr/bin/env python
# coding=utf-8

from Webserver.config import const
from Webserver.common import db_helper

if __name__ == '__main__':
    db ,cursor = db_helper.login_db("root","123456","studentInfo")
    db_helper.create_stu_form(cursor,'student')
    '''
    database, cursor = db_helper.login_db(const.DB_USER, const.DB_PASS, const.DB_NAME)
    db_helper.del_stu_form(cursor)  # 删除student表
    db_helper.create_stu_form(cursor)  # 创建student表
    user_data = {
        'id': 1234,
        'name': 'jf',
        'sex': 'man',
        'contact': '2955xxx'
    }
    db_helper.insert_stu(database, cursor, user_data)  # 加入一个数据
    user_data = {
        'id': 1235,
        'name': 'mahx',
        'sex': 'man',
        'contact': '3211xxx'
    }
    db_helper.insert_stu(database, cursor, user_data)  # 加入一个数据
    print('修改前查询')
    print(db_helper.query_stu(database, cursor, {'name': 'ma'}))    # 查找一个数据
    print(db_helper.query_stu(database, cursor, {'name': 'mahx'}))  # 查找一个数据
    print(db_helper.query_stu(database, cursor, {'id': 1234}))      # 查找一个数据

    user_data = {
        'id': 1235,
        'name': 'mahao',
        'sex': 'man',
        'contact': '3211xxx'
    }
    db_helper.tran_stu(database, cursor, user_data)  # 修改一个数据
    print('修改后查询')
    print(db_helper.query_stu(database, cursor, {'name': 'mahx'}))  # 查找一个数据
    print(db_helper.query_stu(database, cursor, {'name': 'mahao'}))  # 查找一个数据

    user_data = {
        'id': 1234
    }
    print('\n删除前查询')
    print(db_helper.query_stu(database, cursor, {'id': 1234}))  # 查找一个数据
    db_helper.del_stu(database, cursor, user_data)  # 修改一个数据
    print('删除后查询')
    print(db_helper.query_stu(database, cursor, {'id': 1234}))  # 查找一个数据
'''