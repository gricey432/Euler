from math import sqrt
from euler_common import is_prime


def prime_cut_left(n):
    if n < 10:
        return is_prime(n)
    cut = int(str(n)[1:])
    if is_prime(cut):
        return prime_cut_left(cut)
    return False


def prime_cut_right(n):
    if n < 10:
        return is_prime(n)
    cut = int(str(n)[:-1])
    if is_prime(cut):
        return prime_cut_right(cut)
    return False
    

n = 7 # 2, 3, 5, 7 don't count
count = 0
total = 0

# We are told only 11 exist
while count < 11:
    n += 2
    if is_prime(n) and prime_cut_left(n) and prime_cut_right(n):
        count += 1
        total += n

print total
