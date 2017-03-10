import sys

from flask import Flask, request
app = Flask(__name__)

import browser

@app.route('/')
def index():
    url = request.args.get('url')
    if not url:
        url = 'https://github.com/garywu/bitwser'
    sys.stderr.write(url)
    image = browser.get(url)
    return '<html><body><img src="data:image/gif;base64,{}" /></body></html>'.format(image)
