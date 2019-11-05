# -*- coding: utf-8 -*-

import json
from random import *


class GrandPy:
    """ Character creation.
    """

    def __init__(self):
        """ Initialisation.
        """

        # Attribute
        self.query = None
        self.answer = None

    def provide_kick_off_sentence(self, path="GrandPy_BotApp/static/json/GrandPy_answer.json"):
        """ Provide a random sentence.
        """

        try:
            # Open the json file
            with open(path, "r") as read_file:
                random_answer = json.load(read_file)
                # Provide a random number
                random_number = randint(1, len(random_answer) - 1)

            # Define a random sentence from the json file
            self.answer = random_answer["Beginning"][random_number]

        except FileNotFoundError as error:
            raise FileNotFoundError
            print("ERROR")
            print(error)
