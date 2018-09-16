# -*- coding: UTF-8 -*-

import pymysql
import re


#  这个函数用来判断表是否存在
def table_exists(cursor, table_name):
    sql = "show tables;"
    cursor.execute(sql)
    tables = [cursor.fetchall()]
    table_list = re.findall('(\'.*?\')',str(tables))
    table_list = [re.sub("'", '', each) for each in table_list]
    if table_name in table_list:
        # 存在返回1
        return 1
    else:
        return 0


# 提供账户及密码登陆数据库
def login_db(user, pwd, db):
    db = pymysql.connect(host='127.0.0.1', port=3306, user=user, passwd=pwd, db=db, charset="utf8")
    # 获取游标对象
    cursor = db.cursor()
    return {db, cursor}


# 创建表user
def create_user_form(cursor):
    sql_create = "create table user(id int, name varchar(18), pwd varchar(18)) engine = innodb charset = utf8"
    cursor.execute(sql_create)


# 加入新用户
def insert_user(db, cursor, user_id, name, pwd):
    sql_insert = '''insert into user values ("{}", "{}", "{}")'''.format(user_id, name, pwd)
    try:
        cursor.execute(sql_insert)
        db.commit()
    except:
        db.rollback()
