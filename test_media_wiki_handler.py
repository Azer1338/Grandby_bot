# -*- coding: utf-8 -*-
import mediawiki

from GrandPy_BotApp.media_wiki_handler import MediaWikiHandler


def test_api_media_wiki_geosearch(monkeypatch):
    """ test media wiki API for location: Paris
    """

    class MockMediaWiki():
        """ Mock the MediaWiki class
        """

        def __init__(self):
            """No attribute to initialize
            """
            pass

        def set_api_url(self, api_url, lang):
            """ No setup to initialize
            """
            pass

        def geosearch(self, latitude, longitude):
            """ Return a json file.
            """

            place_result = ["Jeux olympiques d'été de 2024",
                            'Ports de Paris',
                            "Deaflympics d'été de 1924",
                            'Hôtel de ville de Paris',
                            "Bibliothèque de l'hôtel de ville de Paris",
                            'Mairie de Paris',
                            'Prise de Paris (1420)',
                            'Bataille de Lutèce (383)',
                            'Siège de Paris (861)',
                            'Siège de Paris (1370)']
            return place_result

    def mock_mediawiki():
        """ Mock the client method of Media Wiki
        """
        return MockMediaWiki()

    # Mock up
    monkeypatch.setattr(mediawiki, 'MediaWiki', mock_mediawiki)

    # Initialise a handler
    handler = MediaWikiHandler()
    handler.provide_closest_place_name_known(48.856614, 2.3522219)

    # Results expected check
    assert handler.place_name == "Jeux olympiques d'été de 2024"


def test_api_media_wiki_opensearch(monkeypatch):
    """ test media wiki API for location: Paris
    """

    class MockMediaWiki():
        """ Mock the MediaWiki class
        """

        def __init__(self):
            """No attribute to initialize
            """
            pass

        def set_api_url(self, api_url, lang):
            """ No setup to initialize
            """
            pass

        def opensearch(self, place):
            """ Return a json file.
            """

            story_result = [('Hôtel de ville de Paris',
                             'L’hôtel de ville de Paris, communément appellé l’Hôtel de Ville, est le bâtiment qui héberge les institutions municipales de Paris depuis 1357.',
                             'https://fr.wikipedia.org/wiki/H%C3%B4tel_de_ville_de_Paris')]
            return story_result

    def mock_mediawiki():
        """ Mock the client method of Media Wiki
        """
        return MockMediaWiki()

    # Mock up
    monkeypatch.setattr(mediawiki, 'MediaWiki', mock_mediawiki)

    # Initialise a handler
    handler = MediaWikiHandler()
    handler.provide_story_about_place()

    # Results expected check
    assert handler.about_sentence == 'L’hôtel de ville de Paris, communément appellé l’Hôtel de Ville, est le bâtiment qui héberge les institutions municipales de Paris depuis 1357.'
