import json,requests
from flask import Flask,request

app = Flask(__name__)

@app.route('/postmethod',methods=['POST'])
def post_json():
    data=request.form
    print(data.text)
    return data

Flask.run(app,host="167.99.186.154")
