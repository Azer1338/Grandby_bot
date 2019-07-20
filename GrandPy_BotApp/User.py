# -*- coding: utf-8 -*-

### User Class
import json

class User():
	""" User's query
	"""

	def __init__(self):
		""" Initialisation.
		"""
		#Attribut
		self.query = None

	def parse_query_method(self):
		""" Keep the major words in a chain.
		"""
		# Load a JSON file
		with open("GrandPy_BotApp/Parse_FR.json", "r") as read_file:
			parse_FR_list = json.load(read_file)
		
		# Convert a chain into list - splitting by " " element
		allWordsList = self.query.split(' ')
		
		# Keep major words using stop-words method
		# Replace parse word by O
		for i, singleWord in enumerate(allWordsList):
			for elmt in parse_FR_list:
				if singleWord == elmt:
					allWordsList[i] = " "

		for b in allWordsList:
			print("La liste parsé est de : " + b);
			
		# Convert a list into chain - adding a " " element
		allWordsChain = " ".join(allWordsList)
		
		# Return User query parsed chain
		self.query = allWordsChain
		
		print(self.query)
