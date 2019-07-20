# -*- coding: utf-8 -*-

from flask import Flask, jsonify, render_template, request

from GrandPy_BotApp.User import User
from GrandPy_BotApp.MediaWiki import MediaWiki
from GrandPy_BotApp.GoogleMapAPI import GoogleMapAPI

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
	
	# Creation a query
	Minot = User()
	
	# Gather the sentence from User
	Minot.query = request.args.get('query')
	
	# Parse it
	Minot.parse_query_method()
	
	# Generate location reference from USer's query
	Place = GoogleMapAPI()
	Place.placeName = Minot.query
	Place.geocode()
	
	# Message
	print("lat: %2.5f || lng: %2.5f" % (Place.lat,Place.lng))
	
	# Return
	return jsonify(result = Minot.query,
					lat = Place.lat,
					lng = Place.lng
					)
