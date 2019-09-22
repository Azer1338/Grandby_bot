from GrandPy_BotApp.google_map_handler import GoogleMapHandler

import googlemaps

from config import API_GOOGLE_KEY


def test_api_google(monkeypatch):
    results = [{
        'address_components':
            [
                {'long_name': 'Paris',
                 'short_name': 'Paris',
                 'types': ['locality', 'political']
                 },
                {'long_name': 'Paris',
                 'short_name': 'Paris',
                 'types': ['administrative_area_level_2', 'political']
                 },
                {'long_name': 'Île-de-France',
                 'short_name': 'Île-de-France',
                 'types': ['administrative_area_level_1', 'political']
                 },
                {'long_name': 'France',
                     'short_name': 'FR',
                     'types': ['country', 'political']
                 }
            ],
        'formatted_address':'Paris, France',
        'geometry':
            {'bounds':
                 {'northeast':
                      {'lat': 48.9021449, 'lng': 2.4699208},
                  'southwest':
                      {'lat': 48.815573, 'lng': 2.224199}
                  },
             'location':
                 {'lat': 48.856614, 'lng': 2.3522219},
             'location_type': 'APPROXIMATE',
             'viewport':
                 {'northeast':
                      {'lat': 48.9021449, 'lng': 2.4699208},
                  'southwest':
                      {'lat': 48.815573, 'lng': 2.224199}
                  }
             },
        'place_id': 'ChIJD7fiBh9u5kcRYJSMaMOCCwQ',
        'types': ['locality', 'political']
    }]

    def mockreturn(request):
        return results



    response = urllib.request.urlopen("http://pplapi.com/batch/{}/sample.json".format(request_count))
    monkeypatch.setattr(urllib.request, 'urlopen', mockreturn)

    geocode_data = googlemaps.Client(key=api_key).geocode(self.place_name)
    monkeypatch.setattr(googlemaps.Client(key=api_key), 'geocode', mockreturn)

    place = GoogleMapHandler(API_GOOGLE_KEY)

    assert script.test_map.geocode('Paris') == results