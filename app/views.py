# -*- coding: utf-8 -*-

from app import app
from flask import render_template

@app.route('/')
def index():
	return render_template('queerhousing.html')

@app.route('/signin')
def signin():
	return render_template('signin.html')

@app.route('/profile')
def profile():
	return render_template('profile.html')