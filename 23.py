from math import sqrt

def sum_of_divisors(n):
    root = int(round(sqrt(n)))
    d = 1
    sum_divisors = 0
    while d <= root:
        if n % d == 0:
            sum_divisors += d if d == n/d else d + n / d
        d += 1
    return sum_divisors - n

abundant_numbers = []
for n in range(1, 28123):
    if sum_of_divisors(n) > n:
        abundant_numbers.append(n)

abundant_sums = []
for a in abundant_numbers:
    for b in abundant_numbers:
        if a + b <= 28123:
            abundant_sums.append(a + b)

# Remove dupes
abundant_sums = list(set(abundant_sums))

sum_of_perfect = 0
for n in range(1, 28123 + 1):
    if n not in abundant_sums:
        sum_of_perfect += n

print sum_of_perfect
