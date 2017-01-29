class PrimeIterator(object):
    def __init__(self):
        self.cache = []
        self._D = {}
        self._q = 2

    def _next_prime(self):
        while True:
            if self._q not in self._D:
                self._D[self._q * self._q] = [self._q]
                self._q += 1
                return self._q - 1
            else:
                for p in self._D[self._q]:
                    self._D.setdefault(p + self._q, []).append(p)
                del self._D[self._q]
            self._q += 1

    def __getitem__(self, i):
        while i >= len(self.cache):
            self.cache.append(self._next_prime())
        return self.cache[i]


def has_n_prime_factors(test_number, n_factors, prime_iterator):
    factors = set()
    for prime in prime_iterator:
        while 1:
            if test_number == prime:
                factors.add(test_number)
                return len(factors) == n_factors
            if test_number % prime is 0:
                # Divide by n and try the same prime again
                test_number /= prime
                factors.add(prime)
                if len(factors) > n_factors:
                    # If we've got more prime factors than needed
                    return False
            else:
                break


n = 646
prev4 = {0: False, -1: False, -2: False, -3: False}
prime_iterator = PrimeIterator()
while True:
    # Rotate
    prev4[-3] = prev4[-2]
    prev4[-2] = prev4[-1]
    prev4[-1] = prev4[0]
    prev4[0] = has_n_prime_factors(n, 4, prime_iterator)

    if prev4[-3] and prev4[-2] and prev4[-1] and prev4[0]:
        print n - 3
        break

    n += 1
