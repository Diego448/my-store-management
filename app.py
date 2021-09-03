from flask import Flask, render_template
from db_utils import get_users, add_user

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/homepage')
def homepage():
    return render_template('homepage.html')

@app.route('/users', methods=['GET','POST'])
def users():
     
    if requests.method == 'GET':
        users = get_users()
        return render_template('users.html', users=users)
    else:
        response = requests.post("http://127.0.0.1:5000", data = {'name': 'Diego', 'password' : '1234'}, headers = {'content-type': 'application/json'})

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
    return response

@app.route('/user/update/<user_id>')
def user_update(user_id):
    return '{}'

@app.route('/user/delete/<user_id>')
def user_delete(user_id):
    return '{}'


