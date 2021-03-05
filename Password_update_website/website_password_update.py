"""
Name: website_password_update.py
Author: Patrick Walsh
Date: 3/5/2021
Purpose: Creates flask web application to run from a web browser, resulting
in a website that lets you navigate between different html files
and external links, including user registration, login, and password
update pages.

Enforces password complexity for passwords and checks passwords for
commonly used passwords. Also logs failed login attempts in .csv file.



Comment: Run following command to generate pylintrc file in directory
where pylint command is being run:
pylint --generate-rcfile | out-file -encoding utf8 .pylintrc

To run the code, you need to set an environmental variable aligned with the file we just created
with the Flask app, and then run flask. In command prompt, navigate to the folder where this file
is located, then run the following commands:

set FLASK_APP=website_password_update.py
flask run

In Powershell:

$env:FLASK_APP = "website_password_update"
flask run
"""

import csv
import string
import socket
from datetime import datetime
from datetime import date
from flask import Flask
from flask import render_template
from flask import request, redirect, session


app = Flask(__name__)  # creates instance of flask class
app.secret_key = 'super_secret_key'


# Must set to local path under /static/ folder
USER_DATABASE = r'C:/Users/pwalsh/Desktop/School/UMGC/SDEV300/Week 8/static/user_database.csv'
COMMON_PASSWORDS = r'C:/Users/pwalsh/Desktop/School/UMGC/SDEV300/Week 8/static/CommonPassword.txt'
LOGS = r'C:/Users/pwalsh/Desktop/School/UMGC/SDEV300/Week 8/static/Logger.csv'


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
    msg = ''  # message that will appear on webpage for password update
    msg_color = 'red'
    if request.method == 'POST':
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        username = request.form.get('username')
        password = request.form.get('password')

        # check if one of the common passwords listed in CommonPassword.txt file
        bad_pass = []
        with open(COMMON_PASSWORDS, "r") as p:
            contents = p.read().splitlines()
            for row in contents:
                bad_pass.append(row)
            if password in bad_pass:
                msg = 'Password too common! Please choose another.'
            # check if password meets requirements
            elif len(password) < 12:
                msg = 'Password must be 12 or more characters in length.'
            elif not any(char.isdigit() for char in password):
                msg = 'Password must contain at least 1 number!'
            elif not any(char.isupper() for char in password):
                msg = 'Password must contain at least 1 uppercase character!'
            elif not any(char.islower() for char in password):
                msg = 'Password must contain at least 1 lowercase character!'
            elif not any(char in string.punctuation for char in password):
                msg = 'Password must contain at least 1 special character!'
            else:
                # Open file
                with open(USER_DATABASE, "a") as f:
                    f.writelines('\n' + first_name + '\t' + last_name + '\t' + username + '\t' + password)
                return redirect('/register_success')

    # points to HTML file
    return render_template('register.html', datetime=str(datetime.now()), msg=msg, msg_color=msg_color)


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
    msg = ''  # message that will appear on webpage for password update
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        with open(USER_DATABASE, "r") as f:
            users = []
            reader = csv.reader(f, delimiter="\t")
            for row in reader:
                users.append(row)
            count = 0
            for i in users:
                count += 1
                if count == 1:  # skip column headers
                    continue
                if i[2] == username:  # if username is correct
                    if i[3] == password:  # if password is correct
                        session['user'] = username
                        return redirect('/login_success')
                else:  # if the username or password does not match
                    # log failed login attempt
                    with open(LOGS, "a") as log:
                        # get date
                        today = date.today()
                        today = str(today)
                        # get time
                        now = datetime.now()
                        current_time = now.strftime("%H:%M:%S")
                        # get IP address
                        hostname = socket.gethostname()
                        ip_add = socket.gethostbyname(hostname)
                        # update log file
                        log.writelines('\n' + today + '\t' + current_time + '\t' + ip_add)
                    msg = 'Wrong username or password'

    # points to HTML file
    return render_template("login.html", datetime=str(datetime.now()), msg=msg)


@app.route('/login_success')  # function decorator shows path of URL
def login_success():
    """
    Loads login success webpage
    """
    if 'user' in session:
        # points to HTML file
        return render_template("login_success.html", datetime=str(datetime.now()))

    # if the user is not in the session
    return '<br><h1><center>You are not logged in.</center></h1>'


@app.route('/update_password', methods=['POST', 'GET'])  # function decorator shows path of URL
def update_password():
    """
    Loads password update webpage
    """
    if 'user' in session:
        # points to HTML file
        current_password = request.form.get('current_password')
        new_password = request.form.get('new_password')
        retype_password = request.form.get('retype_password')
        with open(USER_DATABASE, "r") as f:
            users = []
            msg = ''  # message that will appear on webpage for password update
            msg_color = 'red'
            reader = csv.reader(f, delimiter="\t")
            for row in reader:
                users.append(row)
            count = 0
            for i in users:
                count += 1
                if count == 1:  # skip column headers
                    continue
                if i[2] == session['user']:
                    if i[3] == current_password:  # if current password is correct

                        # check if one of the common passwords listed in CommonPassword.txt file
                        bad_pass = []
                        with open(COMMON_PASSWORDS, "r") as p:
                            contents = p.read().splitlines()
                            for row in contents:
                                bad_pass.append(row)
                            if new_password in bad_pass:
                                msg = 'Password too common! Please choose another.'

                            # check if new password meets requirements
                            elif len(new_password) < 12:
                                msg = 'Password must be 12 or more characters in length.'
                            elif not any(char.isdigit() for char in new_password):
                                msg = 'Password must contain at least 1 number!'
                            elif not any(char.isupper() for char in new_password):
                                msg = 'Password must contain at least 1 uppercase character!'
                            elif not any(char.islower() for char in new_password):
                                msg = 'Password must contain at least 1 lowercase character!'
                            elif not any(char in string.punctuation for char in new_password):
                                msg = 'Password must contain at least 1 special character!'
                            # make sure passwords match
                            elif new_password != retype_password:
                                msg = 'Passwords do not match!'
                            else:
                                # update the password in .csv file
                                update = open(USER_DATABASE, "r")
                                update = ''.join([i for i in update]) \
                                    .replace(current_password, new_password)
                                x = open(USER_DATABASE, "w")
                                x.writelines(update)
                                x.close()

                                msg = 'Password updated!'
                                msg_color = 'green'

                    elif current_password is not None:  # if current password is NOT correct
                        msg = 'Incorrect current password!'

        return render_template("update_password.html", value=session['user'], msg=msg, msg_color=msg_color)

    # if the user is not in the session
    return '<br><h1><center>You are not logged in.</center></h1>'


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
