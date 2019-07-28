# -*- coding: utf-8 -*-

from flask import Flask, jsonify, render_template, request
from mediawiki import MediaWiki

from GrandPy_BotApp.User import User
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
	
	# Gather the sentence from User
	Minot = User()
	Minot.query = request.args.get('query')
	
	# Parse it
	Minot.parse_query_method()
	
	# Generate location reference from User's query
	Place = GoogleMapAPI()
	Place.placeName = Minot.query
	Place.geocode()
	
	# Message
	print("---MAPS---")
	print("lat: %2.5f || lng: %2.5f" % (Place.lat,Place.lng))
	#
	
	# Generation of a MediaWiki instance
	WikiSearch = MediaWiki()
	
	# Set french as language
	WikiSearch.set_api_url(api_url=u'https://fr.wikipedia.org/w/api.php', lang=u'en')

	# Generate the place name from the lat lng
	json_loc = WikiSearch.geosearch(latitude= Place.lat, longitude=Place.lng)

	# Search introduction sentence about the place
	json_search = WikiSearch.opensearch(json_loc[0], results=1)
	
	# Message
	print("---MediaWiki---")
	print(json_loc[0])
	print(json_search[0][1])
	#
	
	# Return
	return jsonify(result = Minot.query,
					lat = Place.lat,
					lng = Place.lng,
					about = json_search[0][1]
					)
