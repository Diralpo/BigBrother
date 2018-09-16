from flask import Flask
from flask import request
from flask_cors import *
from Webserver import login

app = Flask(__name__)
CORS(app,supports_credentials=True)


@app.route('/simple', methods=['GET', 'POST'])
def simple():
    if request.method == 'POST':
        print(request.get_json())
        try:
            result = login.to_login(request.get_json()['name'], request.get_json()['pwd'], "mytest", "user")
            return result
        except:
            return "error"


if __name__ == '__main__':
    app.run(debug=True,port=8080)
