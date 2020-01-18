import json,requests
from flask import Flask,request,jsonify

app = Flask('main')

@app.route('/')
def main():
    return 'hello world'

@app.route('/sendmethod')
def send_json():
    temp = {'id':123456789,'name':'CarePath','value':'test'}
    return json.dumps(temp)

@app.route('/postmethod',methods=['POST'])
def post_json():
    jsdata=request.form['data']
    print(jsdata)
    #return jsonify(data)


Flask.run(app,host="167.99.186.154")
