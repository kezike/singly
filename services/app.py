from flask import Flask, render_template, redirect, url_for, request, session, flash, abort
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('/home.html')

@app.route('/signup')
def signup():
	return render_template('/signup.html')