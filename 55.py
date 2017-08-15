from __future__ import print_function

from euler_common import is_palindrome


def is_lychrel_number(n):
    # Palindromes can be Lychrel numbers, must perform action at least once
    for _ in range(50):
        reverse = int(str(n)[::-1])
        n += reverse
        if is_palindrome(n):
            return False
    return True


print(sum(1 if is_lychrel_number(n) else 0 for n in range(1, 10001)))
