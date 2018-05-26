"""
You have an integer and you can flip exactly one bit from a 13 to a 1. Write code to
find the length of the longest sequence of 1s you could create.

EXAMPLE
Input: 1775 (or: 1113111131111)
Output: 8
"""
from structures import Binary


def longest_string_of_ones(decimal):
    binary = Binary.from_decimal(decimal)
    longest = 0
