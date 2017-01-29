from euler_common import generate_primes, digits
from itertools import permutations, combinations


# Generate all the 4 digit primes
p = []
primes = generate_primes()
prime = primes.next()
while prime < 10000:
    if prime >= 1000:
        p.append(prime)
    prime = primes.next()


def main(p):
    # Iterate through and look for permutations
    for prime in p:
        n = [
            int(''.join(map(str, permutation)))
            for permutation in permutations(digits(prime))
        ]
        if len(n) >= 3:
            for comb in combinations(n, 3):  # don't really need all combinations, but it's quick enough anyway
                if (
                    comb[2] - comb[1] == comb[1] - comb[0]
                    and comb[2] > comb[1]
                    and all(map(lambda x: x >= 1000, comb))
                    and all(map(lambda x: x in p, comb))
                    and 1847 not in comb and 1487 not in comb  # Provided solution
                ):
                    return int(''.join(map(str, comb)))

print main(p)
