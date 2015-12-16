#!/usr/bin/env python3

""" Module to test papers.py  """

__authors__ = "Marcos Armstrong, Paniz Pakravan, Sinisa Savic"
__email__ = "Marcos E-mail, p.pakravan@mail.utoronto.ca, Sinisa E-mail"
__copyright__ = "2015 Susan Sim"
__date__ = "16 December 2015"

__status__ = "Prototype"

# imports one per line
import pytest
import os
from exercise2 import decide

DIR = "test_jsons/"
os.chdir(DIR)


def test_returning():
    """
    Travellers are returning to KAN.
    """
    assert decide("test_returning_citizen.json", "countries.json") ==\
        ["Accept", "Accept", "Quarantine"]










def test_valid_date_format():

    # Will return true
    try:
        valid_date(2011-07-01)
    except MismatchedAttributesException:
        assert True
    else:
        assert MismatchedAttributesException

    # Will return false
    try:
        valid_date(2011.07.01)
    except MismatchedAttributesException:
        assert True
    else:
        MismatchedAttributesException

    # Will return false
    try:
        valid_date(200.7.1)
    except MismatchedAttributesException:
        assert True
    else:
        MismatchedAttributesException








