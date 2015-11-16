import math

def nth_digit(n):
    # Start with a 0 to avoid breaking log
    n += 1
    count = 1
    next_num = 1
    while count < n:
        count += int(math.log10(next_num)) + 1
        next_num += 1
    digits = str(next_num - 1)
    return int(digits[len(digits) - 1 - (count - n)])

print nth_digit(1) * nth_digit(10) * nth_digit(100) * nth_digit(1000) * nth_digit(10000) * nth_digit(100000) * nth_digit(1000000)
