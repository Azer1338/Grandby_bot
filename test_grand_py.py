# -*- coding: utf-8 -*-

from GrandPy_BotApp.grand_py import GrandPy


class TestGrandPy:
    # Definition
    GRANDDAD = GrandPy()

    def test_query(self):
        """ Check the initialisation of attributes.
        """

        assert self.GRANDDAD.query is None

    def test_answer(self):
        """ Check the initialisation of attributes.
        """

        assert self.GRANDDAD.answer is None

    def test_introduction_sentence(self):
        """ Check if a sentence is pick up
        from json file.
        """

        self.GRANDDAD.introduction_sentence()

        assert self.GRANDDAD.answer is not None
