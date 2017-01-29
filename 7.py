from euler_common import is_prime


n = 1  # Starts at 2, 1 added in loop
n_prime = 1

while n_prime <= 10001:
    n += 1
    if is_prime(n):
        n_prime += 1

print n
