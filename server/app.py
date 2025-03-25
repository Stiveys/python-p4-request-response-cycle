#!/usr/bin/env python3

import os

from flask import Flask, request, current_app, g, make_response, jsonify

app = Flask(__name__)

# Request hook that runs before each request
@app.before_request
def app_path():
    g.path = os.path.abspath(os.getcwd())

@app.route('/')
def index():
    host = request.headers.get('Host')
    appname = current_app.name
    response_body = f'''
        <h1>The host for this page is {host}</h1>
        <h2>The name of this application is {appname}</h2>
        <h3>The path of this application on the user's device is {g.path}</h3>
    '''

    status_code = 200
    headers = {}

    return make_response(response_body, status_code, headers)

# Additional route to demonstrate request object properties
@app.route('/request-info')
def request_info():
    # Get information from the request object
    info = {
        'method': request.method,
        'url': request.url,
        'headers': dict(request.headers),
        'args': dict(request.args),
        'remote_addr': request.remote_addr
    }
    return jsonify(info)

# Route demonstrating different status codes
@app.route('/status/<int:code>')
def status_demo(code):
    return f"<h1>Response with status code {code}</h1>", code

if __name__ == '__main__':
    app.run(port=5557, debug=True)  # Changed port from 5556 to 5557
