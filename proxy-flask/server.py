"""
run "pip install flask", or run "pip install -r requirements/flask.txt"
"""

from flask import Flask, request, Response
from flask_cors import CORS, cross_origin
import requests

from .utils import UrlHandling

app = Flask(__name__)
CORS(app)


@app.route('/<path:url>', methods=['GET'])
def mega_proxy_mastermind(url):
    url_to_send = UrlHandling.parse_url(url, 'http://192.168.1.115:8000/')

    r = requests.get(url_to_send, params=request.args)
    return Response(r.text, content_type=r.headers['content-type'])


@app.route('/<path:url>', methods=['POST'])
def mega_proxy_mastermind_post(url):
    url_to_send = UrlHandling.parse_url(url, 'http://192.168.1.115:8000/')

    r = requests.post(url_to_send, params=request.args, data=request.data, headers=request.headers)
    return Response(r.text, content_type=r.headers['content-type'])


@app.route('/<path:url>', methods=['PUT'])
def mega_proxy_mastermind_put(url):
    url_to_send = UrlHandling.parse_url(url, 'http://192.168.1.115:8000/')

    r = requests.put(url_to_send, params=request.args, data=request.data, headers=request.headers)
    return Response(r.text, content_type=r.headers['content-type'])


@app.route('/<path:url>', methods=['DELETE'])
def mega_proxy_mastermind_delete(url):
    url_to_send = UrlHandling.parse_url(url, 'http://192.168.1.115:8000/')

    r = requests.delete(url_to_send)
    return Response(r.text)
