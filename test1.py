import os
import sqlite3
from flask import Flask,render_template,request,session,g,redirect,url_for,abort,flash

app = Flask(__name__)

@app.route("/<name>")
def index(name):

	return render_template('1.html', name=name)

@app.route("/hellooooo")
def hello():
	return "Hello World!"

@app.route("/user/<username>")
def show_user_profile(username):
	return "User %s" %username

@app.route("/post/<int:post_id>")
def show_post(post_id):
	return "Post %d" %post_id



if __name__=="__main__":
	app.run(debug=True)

	