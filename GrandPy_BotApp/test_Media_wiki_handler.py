# -*- coding: utf-8 -*-

from GrandPy_BotApp.Media_wiki_handler import Media_wiki_handler

def test_place_name():
    """ Check the initilisation of attribute
    """
    
    search = Media_wiki_handler()
    
    assert search.place_name == None

def test_about_sentence():
    """ Check the initilisation of attribute
    """
    
    search = Media_wiki_handler()
    
    assert search.about_sentence == None

def test_closest_place_name_known():
    """ Check if an answer from API call is received.
    """
    
    search = Media_wiki_handler()
    search.closest_place_name_known(0,0)
    
    assert search.place_name != None

def test_story_about_place():
    """ Check if an answer from API call is received.
    """
    
    search = Media_wiki_handler()
    search.closest_place_name_known(0,0)
    search.story_about_place()
    
    assert search.place_name != None
