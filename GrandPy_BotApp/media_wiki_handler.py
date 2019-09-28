# -*- coding: utf-8 -*-

from mediawiki import MediaWiki
from random import *


class MediaWikiHandler:
    """ MediaWiki API interface manager.
    """
    
    def __init__(self):
        """ Initialisation.
        """
        self.media_wiki_interface = MediaWiki()
        self.place_name = None
        self.about_sentence = None
        
        # Set french as language
        self.media_wiki_interface.set_api_url(api_url=u'https://fr.wikipedia.org/w/api.php', lang=u'en')

        # For the mock
        self.data = None

    def closest_place_name_known(self, latitude, longitude):
        """ Provide a :self.place_name based
        on :latitude and :longitude.
        """
        
        # API call
        api_json_file = self.media_wiki_interface.geosearch(latitude=latitude, longitude=longitude)

        # In case of the content is empty
        if not api_json_file:
            self.place_name = "Il n'y a pas de lieux connus proches."
        else:
            # Provide a random number
            random_number = randint(0, len(api_json_file)-1)

            # One among all close places
            self.place_name = api_json_file[random_number]

    def story_about_place(self):
        """ Provide a short story related to the :self.place_name.
        """
        
        # API call: Search introduction sentence about the place
        api_json_file = self.media_wiki_interface.opensearch(self.place_name, results=1)

        # In case of the content is empty
        if not api_json_file:
            self.about_sentence = "Oh... rien en fait."
        else:

            self.about_sentence = api_json_file[0][1]

        self.data = api_json_file
