from flask import Flask, render_template
from db_utils import get_users

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/homepage')
def homepage():
    return render_template('homepage.html')

@app.route('/users')
def users():
    users = get_users()
    return render_template('users.html', users=users)

@app.route('/user/list')
def user_list():
    return get_users()

@app.route('/user/<user_id>')
def user_get(user_id):
    response = {'id': user_id}
    return response

@app.route('/user/create')
def user_create():
    return '{}'

@app.route('/user/update/<user_id>')
def user_update(user_id):
    return '{}'

@app.route('/user/delete/<user_id>')
def user_delete(user_id):
    return '{}'


