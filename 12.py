from math import sqrt, ceil

def get_num_divisors(n):
    root = int(ceil(sqrt(n)))
    d = 1
    divisors = 0
    while d <= root:
        if n % d == 0:
            divisors += 1 if d == root else 2
        d += 1
    return divisors

n = 0
c = 1

while True:
    n += c
    if get_num_divisors(n) > 500:
        break
    c += 1

print n
