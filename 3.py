from math import sqrt

num = 600851475143
root = sqrt(num)
i = 1
sum = []

def is_prime(test):
    j = 2
    root = sqrt(test)
    while j <= root:
        if test % j == 0:
            return False
        j += 1
    return True

while i < root:
    i += 1
    if num % i == 0:
        if is_prime(i):
            sum.append(i)
        if is_prime(num / i):
            sum.append(num / i)

print max(sum)
