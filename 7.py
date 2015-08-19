from math import sqrt

def is_prime(test):
    j = 2
    root = sqrt(test)
    while j <= root:
        if test % j == 0:
            return False
        j += 1
    return True

n = 1 # Starts at 2, 1 aded in loop
n_prime = 1

while n_prime <= 10001:
    n += 1
    if is_prime(n):
        n_prime += 1

print n
