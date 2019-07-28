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
		self.query = "Marseille mon amour"

	def parse_query_method(self):
		""" Keep major words using stop-words method.
		"""
		# Load the stop words JSON file
		with open("GrandPy_BotApp/static/json/Parse_FR.json", "r") as read_file:
			parse_FR_list = json.load(read_file)
		
		# Convert a chain into list - splitting by an " "(space) element
		allWordsChain = self.query
		allWordsList = allWordsChain.split(' ')

		# Replace word by "space" word if it is a stop word
		for i, singleWord in enumerate(allWordsList):
			for stop_word in parse_FR_list:
				if singleWord == stop_word:
					allWordsList[i] = "space"
		# Test
		print("---PARSE---")
		print("Before Parse method :")
		for b in allWordsList:
			print(b);
			
		# Convert a list into chain - adding a " "(space) element between them
		allWordsChain = " ".join(allWordsList)
		
		# Replace "space" word by a " " element
		for stopword in parse_FR_list:
			allWordsChain = allWordsChain.replace("space",'')
			
		# Test	
		print("After Parse method : " + allWordsChain)
		
		# Return result
		self.query = allWordsChain
