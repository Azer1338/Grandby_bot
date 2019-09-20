# -*- coding: utf-8 -*-

from GrandPy_BotApp.google_map_handler import googleMapHandler


def test_geocode_lat():
    """ Modify :lat through geocode() use
    """

    home = googleMapHandler()
    home.place_name = "6 Avenue du Ponceau, 95000 Cergy"
    home.geocode()

    assert home.lat == 49.0393601


def test_geocode_lng():
    """ Modify :lng through geocode() use
    """

    home = googleMapHandler()
    home.place_name = "6 Avenue du Ponceau, 95000 Cergy"
    home.geocode()

    assert home.lng == 2.0723879


def test_geocode_address():
    """ Modify :address through geocode() use
    """

    home = googleMapHandler()
    home.place_name = "ENSEA, paris"
    home.geocode()

    assert home.address == "6 Avenue du Ponceau, 95000 Cergy, France"


def test_init_placeName():
    """ Init :placeName correctly
    """

    home = googleMapHandler()

    assert home.place_name is None


def test_init_lat():
    """ Init :lat correctly
    """

    home = googleMapHandler()

    assert home.lat is None


def test_init_lng():
    """ Init :lng correctly
    """

    home = googleMapHandler()

    assert home.lng is None


def test_init_address():
    """ Init :address correctly
    """

    home = googleMapHandler()

    assert home.address is None
