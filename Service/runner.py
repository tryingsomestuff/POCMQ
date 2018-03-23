from flask import Flask
from flask_cors import CORS
from flask import json
from flask import Response

from task import run

from celery.result import AsyncResult

import base64

app = Flask(__name__)
CORS(app)

@app.route('/run/<keyword>')
def runtask(keyword):
    d = base64.b64decode(keyword)
    result = run.apply_async((d,""))
    data = {
        'hello'  : 'world',
        'keyword' : keyword,
        'result' : result.id
    }
    js = json.dumps(data)
    resp = Response(js, status=200, mimetype='application/json')
    return resp

@app.route('/id/<uid>')
def idresult(uid):
    result = AsyncResult(uid)
    try:
        if result.ready():
           data = {
               'hello'  : 'world',
               'id' : uid,
               'result' : result.get(timeout=1)
           }
        else:
           data = { 'state' : 'not ready'}
    except:
        data = { 'state' : 'not ready'}
    js = json.dumps(data)
    resp = Response(js, status=200, mimetype='application/json')
    return resp
