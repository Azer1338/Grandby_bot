# -*- coding: utf-8 -*-

from GrandPy_BotApp.media_wiki_handler import MediaWikiHandler


class TestMediaWikiHandler:
    # Definition
    HANDLER = MediaWikiHandler()

    def test_place_name(self):
        """ Check the initialisation of attribute
        """

        assert self.HANDLER.place_name is None

    def test_about_sentence(self):
        """ Check the initialisation of attribute
        """

        assert self.HANDLER.about_sentence is None

    def test_closest_place_name_known(self):
        """ Check if an answer from API call is received.
        """

        self.HANDLER.closest_place_name_known(0, 0)

        assert self.HANDLER.place_name is not None

    def test_story_about_place(self):
        """ Check if an answer from API call is received.
        """

        self.HANDLER.closest_place_name_known(0, 0)
        self.HANDLER.story_about_place()

        assert self.HANDLER.place_name is not None
