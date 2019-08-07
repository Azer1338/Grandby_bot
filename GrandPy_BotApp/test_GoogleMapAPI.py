# -*- coding: utf-8 -*-

from GrandPy_BotApp.GoogleMapAPI import GoogleMapAPI

def test_geocode_lat():
	""" Modify :lat through geocode() use
	"""
	
	Home = GoogleMapAPI()
	Home.placeName = "6 Avenue du Ponceau, 95000 Cergy"
	Home.geocode()
	
	assert Home.lat == 49.0393601

def test_geocode_lng():
	""" Modify :lng through geocode() use
	"""
	
	Home = GoogleMapAPI()
	Home.placeName = "6 Avenue du Ponceau, 95000 Cergy"
	Home.geocode()
	
	assert Home.lng == 2.0723879

def test_geocode_address():
	""" Modify :address through geocode() use
	"""
	
	Home = GoogleMapAPI()
	Home.placeName = "ENSEA, paris"
	Home.geocode()
	
	assert Home.address == "6 Avenue du Ponceau, 95000 Cergy, France"

def test_init_placeName():
	""" Init :placeName correctly
	"""
	
	Home = GoogleMapAPI()
	
	assert Home.placeName == None

def test_init_lat():
	""" Init :lat correctly
	"""
		
	Home = GoogleMapAPI()
	
	assert Home.lat == None
	
def test_init_lng():
	""" Init :lng correctly
	"""
		
	Home = GoogleMapAPI()
	
	assert Home.lng == None

def test_init_address():
	""" Init :address correctly
	"""
		
	Home = GoogleMapAPI()
	
	assert Home.address == None
