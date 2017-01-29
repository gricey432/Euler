from euler_common import generate_primes, is_prime


primes = generate_primes()
p = []

# Generate a list of primes to sample
while sum(p) < 1000000:
    p.append(primes.next())


# Sample smaller and smaller slices of them
def f(p):
    for l in range(len(p), 0, -1):
        for s in range(0, len(p) - l):
            n = sum(p[s:s+l])
            if is_prime(n):
                return n

print f(p)
