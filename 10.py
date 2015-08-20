from math import sqrt, ceil

def is_prime(test):
    j = 2
    root = int(ceil(sqrt(test)))
    while j <= root:
        if test % j == 0:
            return False
        j += 1
    return True

sum = 0

i = 3
while i < 2000000:
    if is_prime(i):
        sum += i
    i += 2

# Add 2, 2 is the only even prime
print sum + 2
