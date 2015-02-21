from flask import Flask, redirect, url_for, session, request, render_template
from flask_oauth import OAuth


SECRET_KEY = 'development key'
DEBUG = True
FACEBOOK_APP_ID = ''
FACEBOOK_APP_SECRET = ''


app = Flask(__name__)
app.debug = DEBUG
app.secret_key = SECRET_KEY
oauth = OAuth()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/create')
def create():
    return render_template('create.html')

@app.route('/login')
def login():
    return 'logging in'

if __name__ == '__main__':
    app.run()