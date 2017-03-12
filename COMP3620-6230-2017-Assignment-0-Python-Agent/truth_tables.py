# coding=utf-8
""" File name:   truth_tables.py
    Author:      Kuangyi Xing
    Date:        <the date goes here>
    Description: This file defines a number of functions which implement Boolean
                 expressions.

                 It also defines a function to generate and print truth tables
                 using these functions.

                 It should be implemented for Exercise 2 of Assignment 0.

                 See the assignment notes for a description of its contents.
"""
def boolean_fn1(a,b,c):
    """Return truth value of (a ∨ b) → (-a ∧ -b)
    """
    return not(a or b) or (not a and not b)

def boolean_fn2(a,b,c):
    """Return truth value of (a ∧ b) ∨ (-a ∧ -b)
    """
    return (a and b) or (not a and not b)

def boolean_fn3(a,b,c):
    """Return truth value of ((c → a) ∧ (a ∧ -b)) ∨ (-a ∧ b)
    """
    return ((not c or a) and (a and not b)) or (not a and b)

def draw_truth_table(boolean_fn):
    """ This function prints a truth table for the given boolean function.
        It is assumed that the supplied function has three arguments.

        ((bool, bool, bool) -> bool) -> None
    """
    print("{:<7}{:<7}{:<7}{:<7}".format("a","b","c","res"))
    print("------------------------")
    truth = [0,1]
    truth_table = []
    for a in truth:
        for b in truth:
            for c in truth:
                truth_table.append([a,b,c,boolean_fn(a,b,c)])

    for truth_table_row in truth_table :
        print("{:<6} {:<6} {:<6} {:<6}".format(str(bool(truth_table_row[0])),str(bool(truth_table_row[1])),str(bool(truth_table_row[2])),str(bool(truth_table_row[3]))))
