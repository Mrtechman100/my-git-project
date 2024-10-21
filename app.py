from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def home():
	return render_template("indexUP4.html")

@app.route("/about")
def about_me():
	return render_template("aboutme.html")
