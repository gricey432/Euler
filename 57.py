from __future__ import print_function
import sys
from math import log10, ceil

sys.setrecursionlimit(10005)  # I feel awful


def get_fraction(depth):
    # type: (int) -> (int, int)
    if depth == 0:
        return 1, 2

    numerator, denominator = get_fraction(depth - 1)
    numerator += 2 * denominator
    return denominator, numerator  # backwards because of 1/x


longer = 0
for i in range(1, 1001):
    numerator, denominator = get_fraction(i)
    numerator += denominator
    if ceil(log10(numerator)) > ceil(log10(denominator)):
        longer += 1

print(longer)
