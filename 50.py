from math import sqrt, ceil


def primes():
    D = {}
    q = 2
    while True:
        if q not in D:
            yield q
            D[q * q] = [q]
        else:
            for p in D[q]:
                D.setdefault(p + q, []).append(p)
            del D[q]
        q += 1


def is_prime(test):
    j = 2
    root = int(ceil(sqrt(test)))
    while j <= root:
        if test % j == 0:
            return False
        j += 1
    return True


prime_generator = primes()
p = []

# Generate a list of primes to sample
while sum(p) < 1000000:
    p.append(prime_generator.next())


# Sample smaller and smaller slices of them
def f(p):
    for l in range(len(p), 0, -1):
        for s in range(0, len(p) - l):
            n = sum(p[s:s+l])
            if is_prime(n):
                return n

print f(p)
