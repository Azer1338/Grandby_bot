# -*- coding: utf-8 -*-

from GrandPy_BotApp.google_map_handler import GoogleMapHandler

from config import API_GOOGLE_KEY


class TestGoogleMapHandler:
    # Definition
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
