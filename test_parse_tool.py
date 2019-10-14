# -*- coding: utf-8 -*-

from GrandPy_BotApp.parse_tool import *


def test_parsing_method():
    """ Check if the parsing is ok.
    """
    
    query = "abord seraient 12 comparable directement avenue divers mie d'aghonne 31200 huitième Toulouse"
    result = parsing_method(query)

    assert result == "  12   avenue  mie d'aghonne 31200  Toulouse"




def test_parsing_error():
    """ Only low weight words in the query
    """

    query = "abord seraient 12 comparable directement avenue divers mie d'aghonne 31200 huitième Toulouse"
    result = parsing_method(query)

    assert result == "  12   avenue  mie d'aghonne 31200  Toulouse"

def test_parsing_error():
    """ Only high weight words in the query
    """

    query = "abord seraient 12 comparable directement avenue divers mie d'aghonne 31200 huitième Toulouse"
    result = parsing_method(query)

    assert result == "  12   avenue  mie d'aghonne 31200  Toulouse"

def test_parsing_error():
    """ Error - Assert not - logique de test inverse - String
    """

    query = "abord seraient 12 comparable directement avenue divers mie d'aghonne 31200 huitième Toulouse"
    result = parsing_method(query)

    assert not result == " seraient  12   avenue  mie d'aghonne 31200  Toulouse"

def test_parsing_error():
    """ Error - Assert not - logique de test inverse - Integer
    """

    query = "abord seraient 12 comparable directement avenue divers mie d'aghonne 31200 huitième Toulouse"
    result = parsing_method(query)

    assert not result == " seraient  12   avenue  mie d'aghonne 31200  Toulouse"

def test_parsing_error():
    """ word chain empty
    """

    query = "abord seraient 12 comparable directement avenue divers mie d'aghonne 31200 huitième Toulouse"
    result = parsing_method(query)

    assert not result == " seraient  12   avenue  mie d'aghonne 31200  Toulouse"