# -*- coding: utf-8 -*-

from flask import Flask, jsonify, render_template, request

#import Character

app = Flask(__name__)

# Config options - Make sure you created a 'config.py' file.
app.config.from_object('config')
# To get one variable, tape app.config['MY_VARIABLE']

@app.route('/')
@app.route('/index/')
def index():
	
	return render_template('index.html')

@app.route('/result/')
def result():
	
	Man1 = request.args.get('student')
	Man2 = request.args.get('teacher')
	place_requested = request.args.get('place')
	
	place_requested = place_requested + " Such a nice place"
	
	return place_requested
	#return render_template('result.html',user_name = Man1)
    #return jsonify(result="Ou veux tu aller?")
