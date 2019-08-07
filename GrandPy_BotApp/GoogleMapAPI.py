# -*- coding: utf-8 -*-

import googlemaps
from datetime import datetime

class GoogleMapAPI():
	""" Google Map API
		Geocoding Service
		Map service """
		
	def __init__(self):
		""" Initialisation
		"""
		self.placeName = None
		self.lat = None
		self.lng = None
		self.address = None
		self.gmaps = googlemaps.Client(key='AIzaSyAvQ35WfWdo2woLIF4uWCtLdZ0KLwsa0ZE')
		
	def geocode(self):
		""" Provide latitude & longitude from a place name.
		"""

		# Geocoding an address		
		geocode_data = self.gmaps.geocode(self.placeName)
		
		# Grab the lat lng
		self.lat = geocode_data[0]['geometry']['location']['lat']
		self.lng = geocode_data[0]['geometry']['location']['lng']
		
		# Grab the address
		self.address = geocode_data[0]['formatted_address']
