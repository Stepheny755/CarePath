import json,requests

@app.route('/postmethod',methods=['POST'])
def post_json():
    data=request.form
    print(data)
    return data

Flask.run(app,host="167.99.186.154")
