from flask import Flask, render_template, request
from db_utils import get_users, add_user
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
    elif request.method == 'POST':
        response = requests.post("http://127.0.0.1:5000/user/create", data = '{"name": "Diego", "password": "1234"}', headers = {'content-type': 'application/json'})
        return str(response.text)

@app.route('/user/list')
def user_list():
    return get_users()

@app.route('/user/<user_id>')
def user_get(user_id):
    response = {'id': user_id}
    return response

@app.route('/user/create', methods=['POST'])
def user_create():
    response = add_user(request.get_json())
    return {'status': str(response)}

@app.route('/user/update/<user_id>')
def user_update(user_id):
    return '{}'

@app.route('/user/delete/<user_id>')
def user_delete(user_id):
    return '{}'


