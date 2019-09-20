# -*- coding: utf-8 -*-

from GrandPy_BotApp.parse_tool import *


def test_parsing_method():
    """ Check if the parsing is ok.
    """
    
    query = "abord seraient 12 comparable directement avenue divers mie d'aghonne 31200 huitième Toulouse"
    result = parsing_method(query)

    assert result == "  12   avenue  mie d'aghonne 31200  Toulouse"
