# -*- coding: utf-8 -*-

from GrandPy_BotApp.User import User

def test_parse_query_method():
	
	Toto = User()
	Toto.query = "abord seraient 12 comparable directement avenue divers mie d'aghonne 31200 huitième Toulouse"
	Toto.parse_query_method()
	assert Toto.query == "  12   avenue  mie d'aghonne 31200  Toulouse"
