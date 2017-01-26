'''
run "pip install flask", or run "pip install -r requirements/flask.txt"
'''

from flask import Flask, request
app = Flask(__name__)


@app.route('/<path:url>')
def hello_world(url):
    print(request.args)
    print(request.base_url)
    print(request.url)
    print(request.content_type)
    print(request.headers)
    print(request.method)
    return str(url)