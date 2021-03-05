"""
Name: login_website.py
Author: Patrick Walsh
Date: 3/1/2021
Purpose: Creates flask web application to run from a web browser, resulting
in a simple website that lets you navigate between different html files
and external links, including user registration and login pages.

Comment: Run following command to generate pylintrc file in directory
where pylint command is being run:
pylint --generate-rcfile | out-file -encoding utf8 .pylintrc

To run the code, you need to set an environmental variable aligned with the file we just created
with the Flask app, and then run flask. In command prompt, navigate to the folder where this file
is located, then run the following commands:

set FLASK_APP=login_website.py
flask run

In Powershell:

$env:FLASK_APP = "login_website"
flask run
"""

import csv
import string
from datetime import datetime
from flask import Flask
from flask import render_template
from flask import request, redirect, session


app = Flask(__name__)  # creates instance of flask class
app.secret_key = 'super_secret_key'
user_sess = ''  # gets set when user logs in

# Must set to local path under /static/ folder
USER_DATABASE = r'C:/Users/pwalsh/Desktop/School/UMGC/SDEV300/Week 7/static/user_database.csv'


@app.route('/')  # function decorator shows path of URL
def main():
    """
    Loads main webpage
    """
    return render_template('main.html', datetime=str(datetime.now()))


@app.route('/register', methods=['GET', 'POST'])  # function decorator shows path of URL
def register():
    """
    Loads registration webpage
    """
    if request.method == 'POST':
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        username = request.form.get('username')
        password = request.form.get('password')

        # check if password meets requirements
        if len(password) < 12:
            return "<br><h2><center>Password must be 12 or more characters in length.</center></h2>"
        elif not any(char.isdigit() for char in password):
            return "<br><h2><center>Password must contain at least 1 number!</center></h2>"
        elif not any(char.isupper() for char in password):
            return "<br><h2><center>Password must contain at least 1 uppercase character!</center></h2>"
        elif not any(char.islower() for char in password):
            return "<br><h2><center>Password must contain at least 1 lowercase character!</center></h2>"
        elif not any(char in string.punctuation for char in password):
            return "<br><h2><center>Password must contain at least 1 special character!</center></h2>"
        else:
            # Open file
            with open(USER_DATABASE, "a") as f:
                f.writelines('\n' + first_name + '\t' + last_name + '\t' + username + '\t' + password)
            return redirect('/register_success')

    return render_template('register.html', datetime=str(datetime.now()))  # points to HTML file


@app.route('/register_success')  # function decorator shows path of URL
def register_success():
    """
    Loads registration success webpage
    """
    # points to HTML file
    return render_template('register_success.html', datetime=str(datetime.now()))


@app.route('/login', methods=['POST', 'GET'])  # function decorator shows path of URL
def login():
    """
    Loads login webpage
    """
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        with open(USER_DATABASE, "r") as f:
            users = []
            reader = csv.reader(f, delimiter="\t")
            for row in reader:
                users.append(row)
            # print(users)
            count = 0
            for i in users:
                count += 1
                if count == 1:  # skip column headers
                    continue
                # print(i)
                if i[2] == username:
                    # print('username match')
                    if i[3] == password:
                        # print('password match')
                        username = user_sess
                        session['user'] = username
                        return redirect('/login_success')

        # if the username or password does not match
        return "<br><h1><center>Wrong username or password</center></h1>"

    return render_template("login.html", datetime=str(datetime.now()))  # points to HTML file


@app.route('/login_success')  # function decorator shows path of URL
def login_success():
    """
    Loads login success webpage
    """
    if 'user' in session and session['user'] == user_sess:
        # points to HTML file
        return render_template("login_success.html", datetime=str(datetime.now()))

    return '<br><h1><center>You are not logged in.</center></h1>'  # if the user is not in the session


@app.route('/logout')  # function decorator shows path of URL
def logout():
    """
    Logs out and redirects to login page
    """
    session.pop('user')  # remove the session from the browser
    return redirect('/login')


@app.route('/ethics')  # function decorator shows path of URL
def ethics():
    """
    Loads ethics webpage
    """
    return render_template('ethics.html', datetime=str(datetime.now()))  # points to HTML file


@app.route('/my-diet')  # function decorator shows path of URL
def my_diet():
    """
    Loads my-diet webpage
    """
    return render_template('my-diet.html', datetime=str(datetime.now()))  # points to HTML file
