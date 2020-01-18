import json,requests
from flask import Flask,request

app = Flask('main')

@app.route('/')
def main():
    return 'hello world'

Flask.run(app,host="167.99.186.154",port=8080)
