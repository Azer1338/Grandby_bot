# -*- coding: utf-8 -*-

from GrandPy_BotApp.google_map_handler import GoogleMapHandler

from config import API_GOOGLE_KEY


class TestGoogleMapHandler:
    # Definition - Mockable
    HANDLER = GoogleMapHandler(API_GOOGLE_KEY)

    def test_init_place_name(self):
        """ Init :placeName correctly
        """

        assert self.HANDLER.place_name is None

    def test_init_lat(self):
        """ Init :lat correctly
        """

        assert self.HANDLER.lat is None

    def test_init_lng(self):
        """ Init :lng correctly
        """

        assert self.HANDLER.lng is None

    def test_init_address(self):
        """ Init :address correctly
        """

        assert self.HANDLER.address is None

    def test_geocode_lat(self):
        """ Modify :lat through geocode() use
        """
        # Provide an address
        self.HANDLER.place_name = "6 Avenue du Ponceau, 95000 Cergy"
        # Geocode the address
        self.HANDLER.geocode()

        assert self.HANDLER.lat == 49.0393601

    def test_geocode_lng(self):
        """ Modify :lng through geocode() use
        """
        # Provide an address
        self.HANDLER.place_name = "6 Avenue du Ponceau, 95000 Cergy"
        # Geocode the address
        self.HANDLER.geocode()

        assert self.HANDLER.lng == 2.0723879

    def test_geocode_address(self):
        """ Modify :address through geocode() use
        """
        # Provide an address
        self.HANDLER.place_name = "ENSEA, paris"
        # Geocode the address
        self.HANDLER.geocode()

        assert self.HANDLER.address == "6 Avenue du Ponceau, 95000 Cergy, France"

        from GrandPy_BotApp.google_map_handler import GoogleMapHandler

        import googlemaps

        from config import API_GOOGLE_KEY

        def test_api_google(monkeypatch):
            """ test gmap api with paris """

            result = 'Error'

            # result = (48.856614, 2.3522219)

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

