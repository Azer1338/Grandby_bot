# -*- coding: utf-8 -*-

import googlemaps


class GoogleMapHandler:
    """ Google Map API
    Geocode Service
    Map service """

    def __init__(self, api_key):
        """ Initialisation.
        """
        self.place_name = None
        self.lat = None
        self.lng = None
        self.address = None
        self.g_maps = googlemaps.Client(key=api_key)

        self.data = None

    def geocode(self):
        """ Provide latitude & longitude from a place name.
        """

        # Geocode an address
        geocode_data = self.g_maps.geocode(self.place_name)

        # Grab the lat lng
        self.lat = geocode_data[0]['geometry']['location']['lat']
        self.lng = geocode_data[0]['geometry']['location']['lng']

        # Grab the address
        self.address = geocode_data[0]['formatted_address']

        # for Mock
        self.data = geocode_data
from GrandPy_BotApp.google_map_handler import GoogleMapHandler

import googlemaps

from config import API_GOOGLE_KEY


def test_api_google(monkeypatch):
    """ test gmap api with paris """

    result = 'Error'
    #result = (48.856614, 2.3522219)

    def mockreturn(request):
        return result

    monkeypatch.setattr('GrandPy_BotApp.google_map_handler.GoogleMapHandler.geocode', mockreturn)
    api = GoogleMapHandler(API_GOOGLE_KEY)
    api.place_name = 'Marseille'
    assert api.geocode() == result




# def test_api_google(monkeypatch):
#     results = [{
#         'address_components':
#             [
#                 {'long_name': 'Paris',
#                  'short_name': 'Paris',
#                  'types': ['locality', 'political']
#                  },
#                 {'long_name': 'Paris',
#                  'short_name': 'Paris',
#                  'types': ['administrative_area_level_2', 'political']
#                  },
#                 {'long_name': 'Île-de-France',
#                  'short_name': 'Île-de-France',
#                  'types': ['administrative_area_level_1', 'political']
#                  },
#                 {'long_name': 'France',
#                      'short_name': 'FR',
#                      'types': ['country', 'political']
#                  }
#             ],
#         'formatted_address':'Paris, France',
#         'geometry':
#             {'bounds':
#                  {'northeast':
#                       {'lat': 48.9021449, 'lng': 2.4699208},
#                   'southwest':
#                       {'lat': 48.815573, 'lng': 2.224199}
#                   },
#              'location':
#                  {'lat': 48.856614, 'lng': 2.3522219},
#              'location_type': 'APPROXIMATE',
#              'viewport':
#                  {'northeast':
#                       {'lat': 48.9021449, 'lng': 2.4699208},
#                   'southwest':
#                       {'lat': 48.815573, 'lng': 2.224199}
#                   }
#              },
#         'place_id': 'ChIJD7fiBh9u5kcRYJSMaMOCCwQ',
#         'types': ['locality', 'political']
#     }]
#
#     def mockreturn(request):
#         return results
#
#
#
#     response = urllib.request.urlopen("http://pplapi.com/batch/{}/sample.json".format(request_count))
#     monkeypatch.setattr(urllib.request, 'urlopen', mockreturn)
#
#     geocode_data = googlemaps.Client(key=api_key).geocode(self.place_name)
#     monkeypatch.setattr(googlemaps.Client(key=api_key), 'geocode', mockreturn)
#
#     place = GoogleMapHandler(API_GOOGLE_KEY)
#
#     assert script.test_map.geocode('Paris') == results

