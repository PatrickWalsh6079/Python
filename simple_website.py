"""
Name: simple_website.py
Author: Patrick Walsh
Date: 2/19/2021
Purpose: Creates flask web application to run from a web browser, resulting
in a simple website that lets you navigate between different html files
and external links.

Comment: Run following command to generate pylintrc file in directory
where pylint command is being run:
pylint --generate-rcfile | out-file -encoding utf8 .pylintrc

To run the code, you need to set an environmental variable aligned with the file we just created
with the Flask app, and then run flask. In command prompt, navigate to the folder where this file
is located, then run the following commands:

set FLASK_APP=simple_website.py
flask run

In Powershell:

$env:FLASK_APP = "simple_website"
flask run
"""


from datetime import datetime
from flask import Flask
from flask import render_template


app = Flask(__name__)  # creates instance of flask class


@app.route('/')  # function decorator shows path of URL
def main():
    """
    Loads main webpage
    """
    return render_template('main.html', datetime=str(datetime.now()))


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
