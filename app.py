from flask import Flask, render_template, request
import sqlite3
from sqlite3 import Error

app = Flask(__name__)


@app.route('/')
def render_homepage():
    return render_template('home.html')


@app.route('/sign')
def render_sign_page():
    if request.method == 'POST':
        fname = request.form.get('user_fname').title.strip()
        lname = request.form.get('user_fname').title.strip()
        email = request.form.get('user_email').lower().strip()
        password = request.form.get('user_password')
        password2 = request.form.get('user_password2')



    return render_template('sign.html', methods=['POST', 'GET'])


@app.route('/login', methods=['POST', 'GET'])
def render_login_page():
    return render_template('login.html')

@app.route('/about')
def render_about_page():
    return render_template('about.html')
