# -*- coding: utf-8 -*-

from flask import Flask, jsonify, render_template, request
from mediawiki import MediaWiki

from GrandPy_BotApp.Grand_py import Grand_py
from GrandPy_BotApp.Google_map_handler import Google_map_handler
from GrandPy_BotApp.Media_wiki_handler import Media_wiki_handler

from GrandPy_BotApp.Parse_tool import * 

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

        # Generation
        grand_py = Grand_py()
        grand_py.query = request.args.get('query')
        # Parse it
        grand_py.query = parsing_method(grand_py.query)
        # Random sentence from GrandPy
        grand_py.introduction_sentence()
        # Message
        print("------------------------------------")
        print("---GRANDPY---")
        print("GrandPy's answer: " + grand_py.answer)
        print("------------------------------------")

        # Generate location reference from User's query
        place = Google_map_handler()
        place.place_name = grand_py.query
        place.geocode()
        # Message
        print("------------------------------------")
        print("---MAPS---")
        print("lat: %2.5f || lng: %2.5f" % (place.lat, place.lng))
        print("Address: " + place.address)
        print("------------------------------------")

        # Generation of a MediaWiki instance
        place_description = Media_wiki_handler()
        place_description.closest_place_name_known(place.lat, place.lng)
        place_description.story_about_place()
        # Message
        print("------------------------------------")
        print("---MEDIAWIKI---")
        print(place_description.place_name)
        print(place_description.about_sentence)
        print("------------------------------------")

        # Return
        return jsonify( result=grand_py.query,
                        lat=place.lat,
                        lng=place.lng,
                        address=place.address,
                        about=place_description.about_sentence,
                        sentence=grand_py.answer
                        )
