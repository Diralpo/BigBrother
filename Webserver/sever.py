from flask import Flask
from flask import request
from flask_cors import *

app = Flask(__name__)
CORS(app,supports_credentials=True)


@app.route('/simple', methods=['GET', 'POST'])
def simple():
    if request.method == 'POST':
        print(request.get_json())
        return str(request.get_json())


if __name__ == '__main__':
    app.run(debug=True,port=8080)
