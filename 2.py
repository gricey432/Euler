a = 1
b = 1
sum = 0
while b < 4000000:
    sum += b if not b%2 else 0
    b += a
    a = b - a
print sum
