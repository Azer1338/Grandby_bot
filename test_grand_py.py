# -*- coding: utf-8 -*-
import pytest

from GrandPy_BotApp.grand_py import GrandPy


class TestGrandPy:
    # Definition - Mockable
    GRANDDAD = GrandPy()

    # def test_query(self):
    #     """ Check the initialisation of attributes.
    #     """
    #
    #     assert self.GRANDDAD.query is None
    #
    # def test_answer(self):
    #     """ Check the initialisation of attributes.
    #     """
    #
    #     assert self.GRANDDAD.answer is None
    #
    # def test_introduction_sentence(self):
    #     """ Check if a sentence is pick up
    #     from json file.
    #     """
    #
    #     self.GRANDDAD.introduction_sentence()
    #
    #     assert self.GRANDDAD.answer is not None

    def test_introduction_sentence_error(self):
        """test that exception is raised for invalid emails"""
        with pytest.raises(FileNotFoundError) as error:
            assert self.GRANDDAD.introduction_sentence()

def check_email_format(email):
    """check that the entered email format is correct"""
    if not re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", email):
        raise Exception("Invalid email format")
    else:
        return "Email format is ok"

def test_email_exception():
    """test that exception is raised for invalid emails"""
    with pytest.raises(Exception):
        assert check_email_format("good@email.com")