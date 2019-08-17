# -*- coding: utf-8 -*-

from GrandPy_BotApp.Grand_py import Grand_py

def test_query():
    """ Check the initialisation of attributs.
    """
    
    toto = Grand_py()
    
    assert toto.query == None
    
def test_answer():
    """ Check the initialisation of attributs.
    """
    
    toto = Grand_py()
    
    assert toto.answer == None

def test_introduction_sentence():
    """ Check if a sentence is pick up
    from json file.
    """

    toto = Grand_py()
    toto.introduction_sentence()

    assert toto.answer != None
