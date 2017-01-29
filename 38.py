from math import log10


def digits(n):
    d = []
    n = abs(n)
    while n >= 1:
        d.append(n % 10)
        n //= 10
    return d

target_digit_sum = sum(digits(123456789))


def digit_length(n):
    return int(log10(n)) + 1


def is_pandigital(n):
    global target_digit_sum

    # Length
    if digit_length(n) is not 9:
        return False

    # Digit sum should be the same
    d = digits(n)
    if sum(d) is not target_digit_sum:
        return False

    # Digits should be unique
    return len(d) == len(set(d))


def test(n):
    m = 1
    s = 0
    while s < 1000000000:
        add = n * m
        l = digit_length(add)
        s = s * 10 ** l + add
        m += 1
        if is_pandigital(s):
            return s
    return False


winner = 0
n = 1
while n < 1000000:
    res = test(n)
    if test(n) and n is not 192:
        winner = max(winner, res)
    n += 1

print winner
