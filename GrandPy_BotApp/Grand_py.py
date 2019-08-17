# -*- coding: utf-8 -*-

import json
from random import *


class Grand_py:
    """ Character creation.
    """

    def __init__(self):
        """ Initialisation.
        """

        # Attribut
        self.query = None
        self.answer = None

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

        # Convert a list into chain - adding a " "(space) element between them
        allWordsChain = " ".join(allWordsList)

        # Replace "space" word by a " " element
        for stopword in parse_FR_list:
            allWordsChain = allWordsChain.replace("space", '')

        # Return result
        self.query = allWordsChain

    def random_sentence(self):
        """ Provide a random sentence.
        """

        # Open the json file
        with open("GrandPy_BotApp/static/json/GrandPy_answer.json", "r") as read_file:
            random_answer = json.load(read_file)

        # Provide a random number
        random_Number = randint(1, 16)

        # Define a random sentence from the json file
        self.answer = random_answer["Beginning"][random_Number]
