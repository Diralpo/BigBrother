#!/usr/bin/env python
# coding=utf-8

from flask import Flask
from flask import request
from flask_cors import *


from Webserver.common import db_helper
from Webserver.config import const

app = Flask(__name__)
CORS(app, supports_credentials=True)


@app.route('/simple', methods=['GET', 'POST'])
def simple():
    if request.method == 'POST':
        print(request.get_json())
        return str(request.get_json())


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
    app.run(host='0.0.0.0', port=8080)
