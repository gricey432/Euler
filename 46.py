from math import ceil, sqrt


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


def squares():
    n = 1
    while True:
        yield n ** 2
        n += 1


def is_prime(n):
    j = 2
    root = int(ceil(sqrt(n)))
    while j <= root:
        if n % j == 0:
            return False
        j += 1
    return True


def goldbachs_other_conjecture(n):
    for p in primes():
        if p >= n:
            return False
        for s in squares():
            if 2 * s >= n:
                break
            if p + 2 * s == n:
                return True


n = 9
while True:
    n += 2
    if not is_prime(n) and not goldbachs_other_conjecture(n):
        print n
        break
