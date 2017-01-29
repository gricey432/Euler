from euler_common import is_prime

best_l = best_p = 0

for a in range(-999, 1000):
    for b in range(-999, 1000):
        count = 0
        n = 0
        while n * n + a * n + b > 0 and is_prime(n * n + a * n + b):
            n += 1
        if n > best_l:
            best_p = a * b
            best_l = n

print best_p
