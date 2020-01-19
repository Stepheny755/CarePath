import json,requests
from flask import Flask,request

app = Flask(__name__)

@app.route('/',methods=['POST'])
def webhook():
    data=request.form

    print(data)
    return data

Flask.run(app,host="167.99.186.154")
