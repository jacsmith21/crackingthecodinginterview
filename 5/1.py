"""
You are given two 32-bit numbers, N and M, and two bit positions, i and
j. Write a method to insert M into N such that M starts at bit j and ends at bit i. You
can assume that the bits j through i have enough space to fit all of M. That is, if
M = 10011, you can assume that there are at least 5 bits between j and i. You would not, for
example, have j = 3 and i = 2, because M could not fully fit between bit 3 and bit 2.

EXAMPLE
Input: N = 10000000000, M = 10011, i = 2, j = 6
Output: N = 10001001100
"""
from structures import Binary


def add_at_i(N, M, i, j):
    mask = Binary(1 << 32) - 1
    left = mask << (j + 1)
    right = mask >> (32 - i)

    N = N & (left | right)
    return N + (M << i)


assert add_at_i(Binary.from_decimal(10000000000), Binary.from_decimal(10011), 2, 6) == Binary.from_decimal(10001001100)
