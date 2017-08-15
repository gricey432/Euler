from __future__ import print_function, division

from euler_common import is_prime


side_length = 1
end = 1
n_prime_diagonals = 0
n_diagonals = 1
while True:
    side_length += 2
    for _ in range(1, 5):
        end += side_length - 1
        n_diagonals += 1
        if is_prime(end):
            n_prime_diagonals += 1

    if 100 * n_prime_diagonals // n_diagonals < 10:
        break

print(side_length)
