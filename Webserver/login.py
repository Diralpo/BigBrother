# -*- coding: UTF-8 -*-

import pymysql


def to_login(user, pwd, db, table_name):
    conn = pymysql.connect(host='127.0.0.1', user=user, passwd=pwd, db=db)
    cur = conn.cursor()

    # 查询
    sql = "select * from {}".format(table_name)
    re_count = cur.execute(sql)  # 返回受影响的行数
    data = cur.fetchall()  # 返回数据,返回的是tuple类型
    cur.close()
    conn.close()
    print(data)
    return str(re_count)
