# -*- coding: utf-8 -*-

from GrandPy_BotApp.grand_py import grandPy


def test_query():
    """ Check the initialisation of attributs.
    """

    toto = grandPy()

    assert toto.query is None


def test_answer():
    """ Check the initialisation of attributs.
    """

    toto = grandPy()

    assert toto.answer is None


def test_introduction_sentence():
    """ Check if a sentence is pick up
    from json file.
    """

    toto = grandPy()
    toto.introduction_sentence()

    assert toto.answer is not None
