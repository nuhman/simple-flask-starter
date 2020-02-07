import json
from flask import render_template, Response
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Tendulkar'}
    return render_template('index.html', title='Home', user=user)


@app.route('/users')
def users():
    all_users = [
        {'username': 'Tendulkar'},
        {'username': 'Federrer'},
        {'username': 'Modirc'}
    ]
    return Response(json.dumps(all_users), mimetype='application/json')
