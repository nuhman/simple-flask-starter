from flask import render_template, jsonify
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Tendulkar'}
    return render_template('index.html', title='Home', user=user)


@app.route('/api/users')
def users():
    all_users = [
        {'username': 'Tendulkar'},
        {'username': 'Federrer'},
        {'username': 'Modirc'}
    ]
    return jsonify(all_users)
