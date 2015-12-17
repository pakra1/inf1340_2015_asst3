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
# Global constants ##
######################
REQUIRED_FIELDS = ["passport", "first_name", "last_name",
                   "birth_date", "home", "entry_reason", "from"]

######################
# global variables ##
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

    passport_format_regex = re.compile(r"'\w\w\w\w\w - \w\w\w\w\w - \w\w\w\w\w - \w\w\w\w\w")
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

    visa_format_regex = re.compile(r".{5}-.{5}")
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
    year = int(1900 - 2015)
    month = int(01 - 12)
    day = int(01 - 31)

    date_format = re.compile(r"\d\d\d\d-\d\d-\d\d")
    date_string = date_format.search(date_string)
    if year < 1900 or year > 2015:
        return False
    elif month < 01 or month > 12:
        return False
    elif day < 01 or day > 31:
        return False
    else:
        date_string is True


def valid_passport_date(citizen):
    if valid_passport_format(citizen["passport"]) and valid_date_format(citizen["birth_date"]):
        return True
    else:
        return False


def valid_country(citizens):
    """
    Checks if visitor is coming and going to a valid country
    """
    if citizens["home"]["country"] in COUNTRIES and citizens["from"]["country"] in COUNTRIES:
        return True
    else:
        return False


def medical_check(citizens, medical_advisory):
    """
    Checks if visitors are coming from a country that has a medical advisory to know if needed to Quarantine
    """
    if "via" in citizens.keys() and citizens["via"]["country"] in medical_advisory.keys():
        if medical_advisory[citizens["via"]["country"]]["medical_advisory"] == "":
            return False
        else:
            return True
    elif citizens["from"]["country"] in medical_advisory.keys():
        if medical_advisory[citizens["via"]["country"]]["medical_advisory"] == "":
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


def valid_visa(visa):
    return valid_visa_format(visa["code"]) and valid_date_format(visa["date"]) and not is_more_than_x_years_ago(2, visa["date"])


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
        citizens = json.loads(file_contents)

    with open(countries_file, "r") as file_reader:
        countries_contents = file_reader.read()
        countries = json.loads(countries_contents)

    decision = []

    for visitor in citizens:
        if valid_information and valid_passport_date:
            if medical_check(visitor, countries):
                decision.append("Quarantine")
            elif not valid_passport_format(citizens["passport"]):
                decision.append("Reject")
            elif not valid_country(citizens):
                decision.append("Reject")
            elif valid_visa(citizens):
                decision.append("Accept")
            else:
                decision.append("Accept")
        else:
            decision.append("Accept")
    return decision

