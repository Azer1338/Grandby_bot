# -*- coding: utf-8 -*-
import pytest

from GrandPy_BotApp.grand_py import GrandPy


class TestGrandPy:
    """ Test of the grandPy class.
    """

    # Generate an instance
    Granddad = GrandPy()

    def test_query(self):
        """ Check the initialisation of attributes.
        """

        assert self.Granddad.query is None
        assert self.Granddad.answer is None

    def test_introduction_sentence(self):
        """ Check if a sentence is pick up
        from json file.
        """

        self.Granddad.introduction_sentence()

        assert self.Granddad.answer is not None

    def test_introduction_sentence_file_not_found_error(self):
        """ Check that an exception is raised when the path is invalid
        """

        with pytest.raises(FileNotFoundError):
            self.Granddad.introduction_sentence(path="GrandPy_BotApp/static/json/GrandPy_answer2.json")
