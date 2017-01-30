from euler_common import generate_primes

digit_chars = [str(n) for n in range(10)]


def test_prime(prime, primes, primes_len):
    global digit_chars

    # Find all the unique digits in the prime and then swap them out
    primes_digits = set(c for c in str(prime))
    for digit_to_replace in primes_digits:
        base_str = str(prime)
        misses = 0
        for replacement_digit in digit_chars:
            test_str = list(base_str)
            for i in range(primes_len):
                if test_str[i] == digit_to_replace:
                    test_str[i] = replacement_digit
            test_int = int(''.join(test_str))
            if not (test_int in primes and len(test_str) == primes_len):
                misses += 1
                if misses > 2:
                    break

        if misses == (10 - 8):  # 8 is target from problem def
            return prime


def main():
    primes = []
    prime_generator = generate_primes()

    primes_len = 1
    while True:
        # Clear small primes and add new size
        primes = [p for p in primes if p >= 10 ** primes_len]
        while len(primes) == 0 or primes[-1] < 10 ** primes_len:
            primes.append(prime_generator.next())

        # Try different combinations
        for prime in primes:
            if test_prime(prime, primes, primes_len):
                return prime

        primes_len += 1

print main()
