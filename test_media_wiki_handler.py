# -*- coding: utf-8 -*-

from GrandPy_BotApp.media_wiki_handler import mediaWikiHandler


def test_place_name():
    """ Check the initialisation of attribute
    """
    
    search = mediaWikiHandler()
    
    assert search.place_name is None


def test_about_sentence():
    """ Check the initialisation of attribute
    """
    
    search = mediaWikiHandler()
    
    assert search.about_sentence is None


def test_closest_place_name_known():
    """ Check if an answer from API call is received.
    """
    
    search = mediaWikiHandler()
    search.closest_place_name_known(0,0)
    
    assert search.place_name is not None


def test_story_about_place():
    """ Check if an answer from API call is received.
    """
    
    search = mediaWikiHandler()
    search.closest_place_name_known(0,0)
    search.story_about_place()
    
    assert search.place_name is not None
