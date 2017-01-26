'''
run "pip install flask", or run "pip install -r requirements/flask.txt"
'''

from flask import Flask, request, Response
from flask_cors import CORS, cross_origin
import requests
#
app = Flask(__name__)
CORS(app)

def parse_url(url, request, server_route):
    args = ''
    for arg, value in request.args.items():
        args += '?{}={}'.format(arg, value)
    return '{}{}{}'.format(server_route, url, args)

@app.route('/<path:url>')
def mega_proxy_mastermind(url):
    url_to_send = parse_url(url, request, 'http://localhost:8000/')
    r = requests.get(url_to_send)
    return Response(r.text, content_type=r.headers['content-type'])
