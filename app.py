from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello there!"

@app.route('/test')
def test():
    return render_template('homepage.html')