from flask import Flask, render_template
import sqlite3
from sqlite3 import Error

app = Flask(__name__)


@app.route('/')
def render_homepage():
    return render_template('home.html')


@app.route('/sign')
def render_sign_page():
    return render_template('sign.html')


@app.route('/login')
def render_login_page():
    return render_template('login.html')

@app.route('/about')
def render_about_page():
    return render_template('about.html')
