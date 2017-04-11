import os
import sqlite3
from app import app
from flask import Flask,render_template
from .forms import LoginForm

# app = Flask(__name__)
@app.route("/login", methods=["GET","POST"])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		flash('Login requested for OpenID="' + form.openid.data +'",remember_me=' + str(form.remember_me.data))
		return redirect("/index")
	return render_template("login.html",title = "Sign In",form = form)



@app.route("/<name>")
def index(name):

	return render_template('1.html',name=name,title="Valhalla")

@app.route("/index")
def hello():
	return "Hello World!"

@app.route("/user/<username>")
def show_user_profile(username):
	return "User %s" %username

@app.route("/post/<int:post_id>")
def show_post(post_id):
	return "Post %d" %post_id

@app.route("/user")
def show_article():
	user = {"nickname":"Miguel"} #fake name
	posts = [#fake array of posts
		{
			"author":{"nickname":"John"},
			"body": "Beautiful day in Portland!"
		},
		{
			"author":{"nickname":"Susan"},
			"body":"The Avengers movie was so cool!"
		}

	]
	return render_template("1.html",title="Valhalla",user=user,posts=posts,name="Valhalla")


# if __name__=="__main__":
# 	app.run(debug=True)

	