#!/usr/bin/env python3

""" Assignment 3, Exercise 2, INF1340, Fall, 2015. DBMS

This module performs table operations on database tables
implemented as lists of lists. """

__authors__ = "Marcos Armstrong, Paniz Pakravan, Sinisa Savic"
__email__ = "marcos.armstrong@mail.utoronto.ca, p.pakravan@mail.utoronto.ca, sinisa.savic@mail.utoronto.ca"
__date__ = "16 December 2015"


#####################
# HELPER FUNCTIONS ##
#####################

def remove_duplicates(l):
    """
    Removes duplicates from l, where l is a List of Lists.
    :param l: a List
    """

    d = {}
    result = []
    for row in l:
        if tuple(row) not in d:
            result.append(row)
            d[tuple(row)] = True

    return result


class UnknownAttributeException(Exception):
    """
    Raised when attempting set operations on a table
    that does not contain the named attribute
    """
    pass


def selection(t, f):

    """

    Perform select operation on table t that satisfy condition f.

    Example:
    > R = [["A", "B", "C"], [1, 2, 3], [4, 5, 6]]
    ># Define function f that returns True iff
    > # the last element in the row is greater than 3.
    > def f(row): row[-1] > 3
    > select(R, f)
    [["A", "B", "C"], [4, 5, 6]]

    """

    selection_table = []
    # Iterates through table 1
    for row in t:
        if f(row):
            selection_table.append(row)
    # If tables only have one schema column
    if len(selection_table) == 1 or len(selection_table) == 0:
        return None
    else:
        selection_table = remove_duplicates(selection_table)
        return selection_table


def projection(t, r):
    """
    Perform projection operation on table t
    using the attributes subset r.

    Example:
    > R = [["A", "B", "C"], [1, 2, 3], [4, 5, 6]]
    > projection(R, ["A", "C"])
    [["A", "C"], [1, 3], [4, 6]]

    """
    if not t or not r:
        return None
    projection_list = []
    new_list = []
    for i in xrange(len(t[0])):
        for s in xrange(len(r)):
            if r[s] == t[0][i]:
                projection_list.append(i)
            else:
                UnknownAttributeException("Not the same attribution")
    for n in xrange(len(t)):
        new_list.append([t[n][index] for index in projection_list])
    return remove_duplicates(new_list)


def cross_product(t1, t2):
    """
    Return the cross-product of tables t1 and t2.

    Example:
    > R1 = [["A", "B"], [1,2], [3,4]]
    > R2 = [["C", "D"], [5,6]]
    [["A", "B", "C", "D"], [1, 2, 5, 6], [3, 4, 5, 6]]

    """
    row = 1
    column = 1

    # Combine tables
    cross_product_list = [t1[0] + t2[0]]
    while row < len(t1):
        while column < len(t2):
            cross_product_list.append(t1[row] + t2[column])
            column += 1
        column = 1
        row += 1
    # If tables only have one column
    if len(cross_product_list) == 1:
        cross_product_list = None

    return cross_product_list