from euler_common import generate_primes, generate_squares, is_prime


def goldbachs_other_conjecture(n):
    for p in generate_primes():
        if p >= n:
            return False
        for s in generate_squares():
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
