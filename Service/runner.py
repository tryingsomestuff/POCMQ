from flask import Flask
from flask_cors import CORS
from flask import json
from flask import Response

from task import run

from celery.result import AsyncResult

app = Flask(__name__)
CORS(app)

@app.route('/run/<keyword>')
def runtask(keyword):
    result = run.apply_async((keyword,''))
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
    data = {
        'hello'  : 'world',
        'id' : uid,
        'result' : result.get(timeout=300)
    }
    js = json.dumps(data)
    resp = Response(js, status=200, mimetype='application/json')
    return resp
