'''
Created on Jun 1, 2017

@author: duncan
'''
from flask import Flask,render_template, app
from flask.helpers import url_for

app = Flask(__name__)

@app.route("/home/")
def home():
    return  render_template('home.html')

@app.route("/about/")
def about():
    return render_template('about.html')


@app.route("/services/")
def services():
    return  render_template('home.html')


@app.route("/contact/")
def contact():
    return  render_template('home.html')

if __name__=="__main__":
    app.run(host='127.0.0.1', port=8080)
    