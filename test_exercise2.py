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
from exercise2 import decide, valid_passport_format, valid_visa_format, valid_country
from exercise2 import valid_date_format

# DIR = "test_jsons/"
# 0s.chdir(DIR)


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
    assert(valid_passport_format("12A34-56B78-98C76-54D32-12E34")) is True
    assert(valid_passport_format("12345-67890-09876-54321-13579")) is True
    assert(valid_passport_format("1BCDE-2GHIJ-3LMNO-4QRST-5VWXY")) is True
    assert(valid_passport_format("12a34-56b78-98c76-54d32-12e34")) is True
    assert(valid_passport_format("ABCDE-FGHIJ-KLMNO-PQRST-UVWXY")) is True

    assert(valid_passport_format("ABCDEFGHIJKLMNO-PQRST-UVWXY")) is False
    assert(valid_passport_format("12A3456B78-98C7654D32-12E34")) is False



def test_valid_visa_format():
    """
    Visa is valid.
    """
    assert(valid_visa_format("12A34-56B78")) is True
    assert(valid_visa_format("A1234-Z9876")) is True

    assert(valid_visa_format("12AA34-56BB78")) is False
    assert(valid_visa_format("123456-789011")) is False
    assert(valid_visa_format("12A3456BB78")) is False
    assert(valid_visa_format("#2A34-56B78")) is False
    assert(valid_visa_format("12T4512X45")) is False




def test_valid_date_format():
    """
    Date format is valid.
    """
    assert (valid_date_format("2010-10-01")) is True
    assert (valid_date_format("1899-06-29")) is True
    assert (valid_date_format("2003-02-29")) is True

    assert (valid_date_format("15-12-05")) is False
    assert (valid_date_format("2020-12-05")) is False
    assert (valid_date_format("2020-12-05")) is False
    assert (valid_date_format("1999-12-5")) is False
    assert (valid_date_format("1999-2-05")) is False



def test_valid_country():
    """
    Travellers are coming and going to a valid country.
    """
    assert (valid_country("Democratic Republic of Lungary")) is True
    assert (valid_country("democratic republic of lungary")) is True
    assert (valid_country("Kraznoviklandstan")) is True
    assert (valid_country("kraznoviklandstan")) is True
    assert (valid_country("KRAZNOVIKLANDSTAN")) is True

    assert (valid_country("Democratic_Republic/of=Lungary")) is False
    assert (valid_country("Kraznoviklandsta")) is False
    assert (valid_country("Principalities of Fryed")) is False
    assert (valid_country("Democratic Republic of Lungary ")) is False
    assert (valid_country("FRY")) is False


def test_medical_check():
    """
    Visitors are coming from a country that has a medical advisory, to know if needed to Quarantine.
    """
    assert (test_medical_check("Democratic Republic of Lungary", "MUMPS")) is True
    assert (test_medical_check("Kraznoviklandstan", "")) is True
    assert (test_medical_check("Isle of Ii", "")) is True

    assert (test_medical_check("Isle of Iillll", "")) is False
    assert (test_medical_check("Democratic Republic of Lungary", "")) is False








