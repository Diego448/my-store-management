from flask import Flask, render_template, request
from db_utils import get_users, add_user, get_user
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/homepage')
def homepage():
    return render_template('homepage.html')

@app.route('/users', methods=['GET','POST'])
def users():
    if request.method == 'GET':
        users = get_users()
        return render_template('users.html', users=users)

@app.route('/user/list')
def user_list():
    return get_users()

@app.route('/user/<user_id>')
def user_get(user_id):
    response = get_user(user_id)
    return response

@app.route('/user/create', methods=['POST'])
def user_create():
    response = add_user(request.get_json())
    return {'success': str(response)}

@app.route('/user/update/<user_id>')
def user_update(user_id):
    return '{}'

@app.route('/user/delete/<user_id>')
def user_delete(user_id):
    return '{}'


