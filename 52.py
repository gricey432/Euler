from euler_common import digits


def main():
    x = 1  # From puzzle
    while 1:
        multiples = [
            2*x, 3*x, 4*x, 5*x, 6*x
        ]
        digits_x = sorted(digits(x))
        if all(map(lambda a: sorted(a) == digits_x, map(digits, multiples))):
            return x
        x += 1

print main()
