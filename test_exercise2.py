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
from exercise2 import decide, valid_passport_format, valid_visa_format, valid_information, valid_country
from exercise2 import medical_check, visitor_visa_required, valid_date_format

#DIR = "test_jsons/"
#os.chdir(DIR)


def test_returning():
    """
    Travellers are returning to KAN.
    """
    assert decide("test_returning_citizen.json", "countries.json") ==\
        ["Accept", "Accept", "Quarantine"]



def test_valid_passport_format():
    """
    Passport is valid.
    """
    assert(valid_passport_format("12A34-56B78-98C76-54D32-12E34")) == True
    assert(valid_passport_format("12345-67890-09876-54321-13579")) == True
    assert(valid_passport_format("ABCDE-FGHIJ-KLMNO-PQRST-UVWXY")) == False
    assert(valid_passport_format("ABCDEFGHIJKLMNO-PQRST-UVWXY")) == False
    assert(valid_passport_format("1BCDE-2GHIJ-3LMNO-4QRST-5VWXY")) == True
    assert(valid_passport_format("12a34-56b78-98c76-54d32-12e34")) == True
    assert(valid_passport_format("12A3456B78-98C7654D32-12E34")) == False



def test_valid_visa_format():
    """
    Visa is valid.
    """
    assert(valid_visa_format("12A34-56B78")) == True

    assert(valid_visa_format("12AA34-56BB78")) == False
    assert(valid_visa_format("123456-789011")) == False
    assert(valid_visa_format(""))



def test_valid_date_format():
    """
    Date format is valid
    """
    assert(valid_date_format)

    assert (valid_date_format("15-12-05")) == False
    assert (valid_date_format("2020-12-05"))== False
    assert (valid_date_format("2020-12-05"))== False
    assert (valid_date_format("1999-12-5"))== False
    assert (valid_date_format("1999-2-05"))== False
    assert (valid_date_format("2014-SEP-05"))== False
    assert (valid_date_format("2014-SE-05"))== False
    assert (valid_date_format("2014-31-12"))== False

def test_valid_country():
    """
    Travellers are coming and going to a valid country.
    """








