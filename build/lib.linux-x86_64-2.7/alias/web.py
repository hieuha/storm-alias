#!/usr/bin/env python
#coding:utf-8
"""
  Author:  HieUHT --<>
  Purpose: 
  Created: 08/09/2015
"""
import json
import os.path

from flask import (Flask, Response, make_response, jsonify, request,
                   send_from_directory)

from alias import Alias

app = Flask(__name__)


def render(template):
    static_dir = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(static_dir, 'templates', template)
    with open(path) as fobj:
        content = fobj.read()
    return make_response(content)


def response(resp=None, status=200, content_type='application/json'):
    return Response(response=resp, status=status, content_type=content_type)

@app.route('/')
def index():
    return render('index.html')

@app.route('/list', methods=['GET'])
def list_keys():
    return response(json.dumps(app.alias.list_entries()))

@app.route('/update', methods=['PUT'])
def edit():
    try:        
        name = request.json['name']
        command = request.json['command']
        status = request.json['status']
        app.alias.update(name, command, status)
        return response(status=200)
    except ValueError as exc:
        return jsonify(message=exc.message)
    except (KeyError, TypeError):
        return response(status=400)    


@app.route('/delete', methods=['POST'])
def delete():
    try:
        name = request.json['name']
        app.alias.delete(name)
        return response()
    except ValueError as exc:
        return jsonify(message=exc.message), 404
    except (TypeError, ValueError):
        return response(status=400)


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico',
                               mimetype='image/vnd.microsoft.icon')

def run(port, debug = False, profile= '.aliases'):
    port = int(port)
    debug = bool(debug)    
    app.alias = Alias(profile)
    app.run(port=port, debug=debug)
