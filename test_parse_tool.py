# -*- coding: utf-8 -*-
import pytest
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


def test_parsing_empty_chain():
    """ word chain empty
    """

    query = ""
    result = parsing_method(query)

    assert result == ""


def test_parsing_only_integer():
    """ Only Integer in the chain.
    """

    query = "200 1300 0.5 "
    result = parsing_method(query)

    assert result == "200 1300 0.5 "


def test_parsing_inverse_logical():
    """ Check that the input is modified.
    """

    query = "Rue de paris 13"
    result = parsing_method(query)

    assert not result == "Rue de paris 13"


def test_parsing_sentence_file_not_found_error():
    """ Check that an exception is raised when the path is invalid
    """

    with pytest.raises(FileNotFoundError):
        parsing_method("Test", path="GrandPy_BotApp/static/json/Parse_FR2.json")
