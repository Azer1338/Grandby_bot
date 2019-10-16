# -*- coding: utf-8 -*-

from GrandPy_BotApp.parse_tool import *


def test_parsing_method():
    """ Check if the parsing is ok.
    """
    
    query = "abord seraient 12 comparable directement avenue divers mie d'aghonne 31200 huitième Toulouse"
    result = parsing_method(query)

    assert result == "  12   avenue  mie d'aghonne 31200  Toulouse"


def test_parsing_light_words():
    """ Only low weight words in the query
    """

    query = "allo allons allô alors anterieur a  été être ô"
    result = parsing_method(query)

    assert result == "         "


def test_parsing_heavy_words():
    """ Only high weight words in the query
    """

    query = "  12   avenue  mie d'aghonne 31200  Toulouse"
    result = parsing_method(query)

    assert result == "  12   avenue  mie d'aghonne 31200  Toulouse"

# def test_parsing_error():
#     """ Error - Assert not - logique de test inverse - String
#     """
#
#     query = "abord seraient 12 comparable directement avenue divers mie d'aghonne 31200 huitième Toulouse"
#     result = parsing_method(query)
#
#     assert not result == " seraient  12   avenue  mie d'aghonne 31200  Toulouse"
#
# def test_parsing_error():
#     """ Error - Assert not - logique de test inverse - Integer
#     """
#
#     query = "1"
#     result = parsing_method(query)
#
#     assert not result == ""



def test_parsing_empty_chain():
    """ word chain empty
    """

    query = ""
    result = parsing_method(query)

    assert result == ""
