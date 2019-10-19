# -*- coding: utf-8 -*-
import mediawiki

from GrandPy_BotApp.media_wiki_handler import MediaWikiHandler


def test_api_media_wiki(monkeypatch):
    """ test media wiki API for location: Paris """

    class MockMediaWiki():
        """

        """
        def __init__(self):
            pass

        def set_api_url(self, api_url, lang):
            pass

        def geosearch(self, latitude, longitude):

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

        def opensearch(self, place):

            story_result = [('Hôtel de ville de Paris',
                             'L’hôtel de ville de Paris, communément appellé l’Hôtel de Ville, est le bâtiment qui héberge les institutions municipales de Paris depuis 1357.',
                             'https://fr.wikipedia.org/wiki/H%C3%B4tel_de_ville_de_Paris')]
            return story_result

    def mock_mediawiki():
        return MockMediaWiki()

    monkeypatch.setattr(mediawiki, 'MediaWiki', mock_mediawiki)

    # Let's go
    handler = MediaWikiHandler()
    handler.closest_place_name_known(48.856614, 2.3522219)
    handler.story_about_place()

    assert handler.place_name == "Jeux olympiques d'été de 2024"
    assert handler.about_sentence == 'L’hôtel de ville de Paris, communément appellé l’Hôtel de Ville, est le bâtiment qui héberge les institutions municipales de Paris depuis 1357.'
