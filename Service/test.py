from flask import Flask
from flask_cors import CORS
from flask import json
from flask import Response

app = Flask(__name__)
CORS(app)

@app.route('/<keyword>')
def show_user_profile(keyword):
    data = {
        'hello'  : 'world',
        'keyword' : keyword
    }
    js = json.dumps(data)
    return js
