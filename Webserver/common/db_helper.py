#!/usr/bin/env python
# coding=utf-8

import pymysql
import re

from Webserver.config import const
from Webserver.common import mail_sent


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
    # 首先检测此数据库是否存在
    if database_exists(cursor, db_name) is 1:
        sql_create = "drop database {}".format(db_name)
        cursor.execute(sql_create)


# 提供账户及密码登陆数据库
def login_db(user, pwd, db_name):
    try:
        db = pymysql.connect(host=const.DB_HOST, port=const.DB_PORT, user=user, passwd=pwd, db=db_name, charset="utf8", cursorclass = pymysql.cursors.DictCursor)
        # 获取游标对象
        cursor = db.cursor()
        return db, cursor
    except pymysql.err.InternalError:
        # 若该数据库不存在
        db = pymysql.connect(host=const.DB_HOST, port=const.DB_PORT, user=user, passwd=pwd, db='mysql', charset="utf8")
        # 获取游标对象
        cursor = db.cursor()
        create_database(cursor, db_name)

        db = pymysql.connect(host=const.DB_HOST, port=const.DB_PORT, user=user, passwd=pwd, db=db_name, charset="utf8", cursorclass = pymysql.cursors.DictCursor)
        # 获取游标对象
        cursor = db.cursor()
        return db, cursor


# 创建表student
# 未以一个自增长的属性作为主码，直接使用学号
def create_stu_form(cursor, table_name='student'):
    # 首先检测表单是否存在
    if table_exists(cursor, table_name) is 0:
        sql_create = "create table {}(id INT PRIMARY KEY, name varchar(18) NOT NULL, " \
                     "sex ENUM('man','woman') NOT NULL, contact varchar(30))".format(table_name)
        cursor.execute(sql_create)


# 删除表student
def del_stu_form(cursor, table_name='student'):
    # 首先检测表单是否存在
    if table_exists(cursor, table_name) is 1:
        sql_create = "drop table {}".format(table_name)
        cursor.execute(sql_create)


############################
#  加入新用户
#  需传入一个字典，包含
#   id
#   name
#   sex     : 性别
#   contact : 联系方式(可缺少)
def insert_stu(db, cursor, user_data):
    try:
        stu_id = user_data['id']
        name = user_data['name']
        sex = user_data['sex']
        try:
            contact = user_data['contact']
            sql_insert = '''insert into student(id, name, sex, contact) values ({}, "{}", "{}", "{}")'''.format(stu_id, name, sex, contact)
        except KeyError:
            # 传入的字典中无contact 字段
            sql_insert = '''insert into student(id, name, sex) values ({}, "{}", "{}")'''.format(stu_id, name, sex)
    except KeyError:
        # 不可缺少的字段缺失，结束程序
        # mail_sent.mail('加入学生信息', "表单要素缺失\n{}".format(str(user_data)))
        return -1
    try:
        cursor.execute(sql_insert)
        db.commit()
        return 0
    except :
        db.rollback()
    return -1


#####################
# 查询某个学生信息
# 返回一个元组对象
def query_stu(db, cursor, user_data):
    try:
        stu_id = user_data['id']
        if stu_id is "":
            sql = "select * from student where id={}".format(stu_id)
            cursor.execute(sql)
            res = cursor.fetchall()
        else:
            stu_name = user_data['name']
            sql = "select * from student where name like '{}'".format(stu_name)
            cursor.execute(sql)
            res = cursor.fetchall()
        return res
    except KeyError:
        # 无学号信息，不支持按姓名删除
        # mail_sent.mail('查询学生信息', "表单要素缺失\n{}".format(str(user_data)))
        return None
    except:
        return None


#####################
# 删除某个学生信息
def del_stu(db, cursor, user_data):
    try:
        stu_id = user_data['id']
        sql = "delete from student where id={}".format(stu_id)
        cursor.execute(sql)
        db.commit()
        return 0
    except KeyError:
        # 无学号信息，不支持按姓名删除
        return -1
    except:
        return -2


#####################
# 修改某个学生信息
def tran_stu(db, cursor, user_data):
    try:
        stu_id = user_data['id']
        name = user_data['name']
        sex = user_data['sex']
        try:
            contact = user_data['contact']
            sql_insert = '''update student set name='{}',sex = '{}',contact ='{}' where id={}'''.format(
                name, sex, contact, stu_id)
        except KeyError:
            # 传入的字典中无contact 字段
            sql_insert = '''update student set name='{}',sex = '{}' where id={}'''.format(
                name, sex, stu_id)
    except KeyError:
        # 不可缺少的字段缺失，结束程序
        # mail_sent.mail('修改学生信息', "表单要素缺失\n{}".format(str(user_data)))
        return -1
    except:
        return -2
    try:
        cursor.execute(sql_insert)
        db.commit()
        return 0
    except :
        db.rollback()
    return -1
