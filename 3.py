from euler_common import is_prime
from math import sqrt

num = 600851475143
root = sqrt(num)
i = 1
sum = []

while i < root:
    i += 1
    if num % i == 0:
        if is_prime(i):
            sum.append(i)
        if is_prime(num / i):
            sum.append(num / i)

print max(sum)
