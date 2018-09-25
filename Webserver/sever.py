#!/usr/bin/env python
# coding=utf-8

from flask import Flask
from flask import request
from flask import render_template
from flask_cors import *


from Webserver.common import db_helper
from Webserver.config import const

app = Flask(__name__, template_folder='../Webpage/')
CORS(app, supports_credentials=True)


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/search', methods=['GET', 'POST'])
def search():

        student = request.get_json()
        res = db_helper.query_stu(db,cursor,student)
        if res==None or res == ():
            print("无查询结果")
            return ""
        print(res)
        return str(res[0]).replace("\'", "\"")


@app.route('/delete', methods=['GET', 'POST'])
def delete():
    data = request.get_json()
    res = db_helper.del_stu(db,cursor,data)
    if res==0:
        print("删除成功")
    else:
        print("删除失败")
    return str(res)


@app.route('/signUp', methods=['GET', 'POST'])
def signUp():
    data = request.get_json()
    res = db_helper.insert_stu(db,cursor,data)
    if res==0:
        print("新建用户成功")
    else:
        print("新建用户失败")
    return str(res)


@app.route('/change', methods=['GET', 'POST'])
def change():
    data = request.get_json()
    res = db_helper.tran_stu(db,cursor,data)
    if res==0:
        print("更新用户信息成功")
    else:
        print("更新用户信息失败")
    return str(res)


if __name__ == '__main__':
    #app.run(debug=True,port=8080)
    db, cursor = db_helper.login_db(const.DB_USER, const.DB_PASS, const.DB_NAME)
    app.run(host='127.0.0.1', port=8080)
