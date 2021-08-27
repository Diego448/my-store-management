from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/homepage')
def homepage():
    return render_template('homepage.html')

@app.route('/users')
def users():
    return render_template('users.html')

@app.route('/user/list')
def user_list():
    return '{}'

@app.route('/user/<user_id>')
def user_get(user_id):
    response = {'id': user_id}
    return response

@app.route('/user/create')
def user_create():
    return '{}'

@app.route('/user/update')
def user_update():
    return '{}'

@app.route('/user/delete')
def user_delete():
    return '{}'


