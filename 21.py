from math import sqrt, ceil

def sum_of_divisors(n):
    root = int(ceil(sqrt(n)))
    d = 1
    sum_divisors = 0
    while d <= root:
        if n % d == 0:
            sum_divisors += d if d == root else d + n / d
        d += 1
    return sum_divisors - n

amicable_sum = 0

for n in range(1, 10000):
    a = sum_of_divisors(n)
    b = sum_of_divisors(a)
    if n == b and a != n:
        amicable_sum += n

print amicable_sum
