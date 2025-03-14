from flask import Flask, render_template, request, redirect, session
import sqlite3
from sqlite3 import Error

app = Flask(__name__)

DATABASE = 'project'


def connect_database(db_file):
    try:
        connection = sqlite3.connect(db_file)
        return connection
    except Error as e:
        print(e)
        print("Error")
    return

@app.route('/')
def render_homepage():
    return render_template('home.html')


@app.route('/sign',methods=['POST', 'GET'])
def render_sign_page():
    if request.method == 'POST':
        fname = request.form.get('user_fname').title().strip()
        lname = request.form.get('user_fname').title().strip()
        email = request.form.get('user_email').lower().strip()
        password = request.form.get('user_password')
        password2 = request.form.get('user_password2')

        if password != password2:
            return redirect("\sign?error=passwords+do+not+match")

        if len(password) < 8:
            return redirect("\sign?error=password+must+be+8+long")

        con = connect_database(DATABASE)

        query_insert = "INSERT INTO user (fname, lname, email, password) VALUES (?, ?, ?, ?,)"
        cur = con.cursor()
        cur.execute(query_insert, (fname, lname, email, password))
        con.commit()
        con.close()

    return render_template('sign.html')




@app.route('/login', methods=['POST', 'GET'])
def render_login_page():
    return render_template('login.html')


    session['user_id'] = user_info[0]
    session['email'] = user_info[1]

@app.route('/about')
def render_about_page():
    return render_template('about.html')
