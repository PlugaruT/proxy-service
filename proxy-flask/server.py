'''
run "pip install flask", or run "pip install -r requirements/flask.txt"
'''

from flask import Flask, request, Response
from flask_cors import CORS
import requests

from utils import UrlHandling

app = Flask(__name__)
CORS(app)


@app.route('/<path:url>')
def mega_proxy_mastermind(url):
    url_to_send = UrlHandling.parse_url(url, request, 'http://localhost:8000/')
    r = requests.get(url_to_send)
    return Response(r.text, content_type=r.headers['content-type'])
