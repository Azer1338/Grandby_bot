# -*- coding: utf-8 -*-
import googlemaps

from GrandPy_BotApp.google_map_handler import GoogleMapHandler

from config import API_GOOGLE_KEY


def test_api_google(monkeypatch):
    """ test media wiki API for location: Paris """

    class MockGoogleClient():
        """Mock up of the GOOGLE API Client"""
        def __init__(self):
            """"""

        def geocode(self,place):

            coordinates_result = [{'address_components': [{'long_name': 'Paris',
                                                           'short_name': 'Paris',
                                                           'types': ['locality',
                                                                     'political']},
                                                          {'long_name': 'Paris',
                                                           'short_name': 'Paris',
                                                           'types': ['administrative_area_level_2',
                                                                     'political']},
                                                          {'long_name': 'Île-de-France',
                                                           'short_name': 'Île-de-France',
                                                           'types': ['administrative_area_level_1',
                                                                     'political']},
                                                          {'long_name': 'France',
                                                           'short_name': 'FR',
                                                           'types': ['country',
                                                                     'political']}],
                                   'formatted_address': 'Paris, France',
                                   'geometry': {'bounds': {'northeast': {'lat': 48.9021449,
                                                                         'lng': 2.4699208},
                                                           'southwest': {'lat': 48.815573,
                                                                         'lng': 2.224199}},
                                                'location': {'lat': 48.856614,
                                                             'lng': 2.3522219},
                                                'location_type': 'APPROXIMATE',
                                                'viewport': {'northeast': {'lat': 48.9021449,
                                                                           'lng': 2.4699208},
                                                             'southwest': {'lat': 48.815573,
                                                                           'lng': 2.224199}}},
                                   'place_id': 'ChIJD7fiBh9u5kcRYJSMaMOCCwQ',
                                   'types': ['locality',
                                             'political']}]

            return coordinates_result


    def mock_client(key):
        mock = MockGoogleClient()

        return mock

    monkeypatch.setattr(googlemaps, 'Client', mock_client)

    handler = GoogleMapHandler(API_GOOGLE_KEY)
    handler.geocode()

    assert handler.lat == 48.856614
    assert handler.lng == 2.3522219
    assert handler.address == 'Paris, France'
