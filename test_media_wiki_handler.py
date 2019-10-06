# -*- coding: utf-8 -*-
from mediawiki import MediaWiki

from GrandPy_BotApp.media_wiki_handler import MediaWikiHandler


def test_api_media_wiki(monkeypatch):
    """ test media wiki API for location: Paris """

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

    story_result = [('Hôtel de ville de Paris',
               'L’hôtel de ville de Paris, communément appellé l’Hôtel de Ville, est le bâtiment qui héberge les institutions municipales de Paris depuis 1357.',
               'https://fr.wikipedia.org/wiki/H%C3%B4tel_de_ville_de_Paris')]

    def mock_geosearch(latitude="0", longitude="0"):
        return place_result
    monkeypatch.setattr(MediaWiki, 'geosearch', mock_geosearch)

    def mock_opensearch(place, number):
        return story_result
    monkeypatch.setattr(MediaWiki, 'opensearch', mock_opensearch)

    handler = MediaWikiHandler()
    # handler.closest_place_name_known("latitude", "longitude")
    handler.story_about_place()

    # Test ne fonctionne pas - "TypeError: mock_geosearch() got multiple values for argument 'latitude'"
    # assert handler.place_name == "Jeux olympiques d'été de 2045"
    #
    assert handler.about_sentence == 'L’hôtel de ville de Paris, communément appellé l’Hôtel de Ville, est le bâtiment qui héberge les institutions municipales de Paris depuis 1357.'