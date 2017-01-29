from math import sqrt, ceil


def generate_primes():
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


def is_prime(n):
    j = 2
    root = int(ceil(sqrt(n)))
    while j <= root:
        if n % j == 0:
            return False
        j += 1
    return True


def generate_squares():
    n = 1
    while True:
        yield n ** 2
        n += 1


def digits(n):
    d = []
    n = abs(n)
    while n >= 1:
        d.append(n % 10)
        n //= 10
    return d
