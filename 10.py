from euler_common import is_prime

total = 0

i = 3
while i < 2000000:
    if is_prime(i):
        total += i
    i += 2

# Add 2, 2 is the only even prime
print total + 2
