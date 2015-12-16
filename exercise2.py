#!/usr/bin/env python3

""" Assignment 3, Exercise 2, INF1340, Fall, 2015. Kanadia

Computer-based immigration office for Kanadia

"""

__authors__ = "Marcos Armstrong, Paniz Pakravan, Sinisa Savic"
__email__ = "Marcos E-mail, p.pakravan@mail.utoronto.ca, Sinisa E-mail"
__copyright__ = "2015 Susan Sim"
__date__ = "16 December 2015"

import re
import datetime
import json


######################
## global constants ##
######################
REQUIRED_FIELDS = ["passport", "first_name", "last_name",
                   "birth_date", "home", "entry_reason", "from"]

######################
## global variables ##
######################
'''
countries:
dictionary mapping country codes (lowercase strings) to dictionaries
containing the following keys:
"code","name","visitor_visa_required",
"transit_visa_required","medical_advisory"
'''
COUNTRIES = None

#####################
# HELPER FUNCTIONS ##
#####################
def is_more_than_x_years_ago(x, date_string):
    """
    Check if date is less than x years ago.

    :param x: int representing years
    :param date_string: a date string in format "YYYY-mm-dd"
    :return: True if date is less than x years ago; False otherwise.
    """

    now = datetime.datetime.now()
    x_years_ago = now.replace(year=now.year - x)
    date = datetime.datetime.strptime(date_string, '%Y-%m-%d')

    return (date - x_years_ago).total_seconds() < 0

def valid_passport_format(passport_number):
    """
    Checks whether a passport number is five sets of five alpha-number characters separated by dashes
    :param passport_number: alpha-numeric string
    :return: Boolean; True if the format is valid, False otherwise
    """

    passport_format_regex= re.compile(r".{5}-.{5}-.{5}-.{5}-.{5}")
    passport_number == passport_format_regex.search(passport_number)
    if passport_number is None:
        passport = False
    else:
        passport = True
    return passport


def valid_visa_format(visa_code):
    """
    Checks whether a visa code is two groups of five alphanumeric characters
    :param visa_code: alphanumeric string
    :return: Boolean; True if the format is valid, False otherwise

    """

    visa_format_regex= re.compile(r".{5}-.{5}")
    visa_code == visa_format_regex.search(visa_code)
    if visa_code is None:
        visa = False
    else:
        visa = True
    return visa


def valid_date_format(date_string):
    """
    Checks whether a date has the format YYYY-mm-dd in numbers
    :param date_string: date to be checked
    :return: Boolean True if the format is valid, False otherwise
    """

    date_format = re.compile(r"\d\d\d\d-\d\d-\d\d")
    date_match = date_format.search(date_string)
    if date_match is None:
        date = False
    else:
        date = True
    return date


def valid_country(Citizens, Countries):
    """
    Checks if visitor is coming and going to a valid country
    """
    if Citizens["home"]["country"] in Countries.keys() and Citizens["from"]["country"] in Countries.keys():
        return True
    else:
        return False


def medical_check(Citizens, medical_advisory):
    """
    Checks if visitors are coming from a country that has a medical advisory to know if needed to Quarantine
    """
    if "via" in Citizens.keys() and Citizens["via"]["country"] in medical_advisory.keys():
        if medical_advisory[Citizens["via"]["country"]]["medical_advisory"] == "":
            return False
        else:
            return True
    elif Citizens["from"]["country"] in medical_advisory.keys():
        if medical_advisory[Citizens["via"]["country"]]["medical_advisory"] == "":
            return False
        else:
            return True
    else:
        return False


def valid_information(credentials):
    if not credentials["passport"]:
        return False
    elif not credentials["first_name"]:
        return False
    elif not credentials["last_name"]:
        return False
    elif not credentials["birth_date"]:
        return False
    elif not credentials["home"]:
        return False
    elif not credentials["entry_reason"]:
        return False
    elif not credentials["from"]:
        return False
    else:
        return True


def visitor_visa_required(visa, valid_country_format):

    # Checks if visitor has a passport from a country from which a visa is required.

    if visa["home"]["country"] in valid_country_format.keys():
        country_visa = visa["home"]["country"]
        if valid_country_format[country_visa]["visitor_visa_required"] == 0:
            return False
        else:
            return True

def decide(input_file, countries_file):
    """
    Decides whether a traveller's entry into Kanadia should be accepted

    :param input_file: The name of a JSON formatted file that contains
        cases to decide
    :param countries_file: The name of a JSON formatted file that contains
        country data, such as whether an entry or transit visa is required,
        and whether there is currently a medical advisory
    :return: List of strings. Possible values of strings are:
        "Accept", "Reject", and "Quarantine"
    """
    with open(input_file, "r") as file_reader:
        file_contents = file_reader.read()
        Citizens = json.loads(file_contents)

    with open(countries_file, "r") as file_reader:
        countries_contents = file_reader.read()
        Countries = json.loads(countries_contents)



