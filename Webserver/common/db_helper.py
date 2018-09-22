#!/usr/bin/env python
# coding=utf-8

import pymysql
import re

from Webserver.config import const


#  查找是否具有某数据库
def database_exists(cursor, db_name):
    sql = "show databases;"
    cursor.execute(sql)
    tables = [cursor.fetchall()]
    table_list = re.findall('(\'.*?\')', str(tables))
    table_list = [re.sub("'", '', each) for each in table_list]
    if db_name in table_list:
        # 存在返回1
        return 1
    else:
        return 0


#  这个函数用来判断表是否存在
def table_exists(cursor, table_name):
    sql = "show tables;"
    cursor.execute(sql)
    tables = [cursor.fetchall()]
    table_list = re.findall('(\'.*?\')', str(tables))
    table_list = [re.sub("'", '', each) for each in table_list]
    if table_name in table_list:
        # 存在返回1
        return 1
    else:
        return 0


#  创建新的库
def create_database(cursor, db_name):
    # 首先检测此数据库是否存在
    if database_exists(cursor, db_name) is 0:
        sql_create = "create database {}".format(db_name)
        cursor.execute(sql_create)


#  删除某数据库
def del_database(cursor, db_name):
    sql_create = "drop database if exists {}".format(db_name)
    cursor.execute(sql_create)


# 提供账户及密码登陆数据库
def login_db(user, pwd, db):
    db = pymysql.connect(host=const.DB_HOST, port=const.DB_PORT, user=user, passwd=pwd, db=db, charset="utf8")
    # 获取游标对象
    cursor = db.cursor()
    return [db, cursor]


# 创建表student
def create_user_form(cursor):
    sql_create = "create table student(id int, name varchar(18), pwd varchar(18)) engine = innodb charset = utf8"
    cursor.execute(sql_create)


# 加入新用户
def insert_user(db, cursor, user_id, name, pwd):
    sql_insert = '''insert into student values ("{}", "{}", "{}")'''.format(user_id, name, pwd)
    try:
        cursor.execute(sql_insert)
        db.commit()
    except:
        db.rollback()
