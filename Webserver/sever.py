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


@app.route('/login', methods=['GET', 'POST'])
def main_sign_in():
    if request.method == 'POST':
        print(request.get_json())
        try:
            db, cursor = db_helper.login_db(request.get_json()['name'], request.get_json()['pwd'], const.DB_NAME)
            print('success')
            return 'success'
        except:
            return "error"


@app.route('/signup', methods=['GET', 'POST'])
def main_sign_up():
    print("待定")


if __name__ == '__main__':
    #app.run(debug=True,port=8080)
    db, cursor = db_helper.login_db(const.DB_USER, const.DB_PASS, const.DB_NAME)
    app.run(host='127.0.0.1', port=8080)
