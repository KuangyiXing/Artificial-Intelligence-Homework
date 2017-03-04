""" File name:   math_functions.py
Author:      Kuangyi Xing
    Date:       2017/03/04
    Description: This file defines a set of variables and simple functions.

                 It should be implemented for Exercise 1 of Assignment 0.

                 See the assignment notes for a description of its contents.
"""
import math
ln_e = math.log(math.exp(1))
twenty_radians = math.radians(20)
def quotient_ceil(numerator,denominator):
    """Return the value of ceiling of numerator divided by denominator
       (number) -> int
    """
    return math.ceil(numerator/denominator)

def quotient_floor(numerator,denominator):
    """Return the value of floor of numerator divided by denominator
       (number) -> int
    """
    return math.floor(numerator/denominator)

def manhattan(x1,y1,x2,y2):
    """Return the manhattan distance between (x1,y1) and (x2,y2)
       (number) -> number
    """
    return math.fabs(x1-x2) + math.fabs(y1-y2)
