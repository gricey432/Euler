from math import sqrt
from euler_common import is_prime


def digit_rotations(n):
    s = list(str(n))
    result = []
    for i in range(len(s)):
        s.append(s[0])
        del s[0]
        result.append(int(''.join(s)))
    return result


count = 0

for n in range(1000000):
    is_circular = True
    for r in digit_rotations(n):
        if not is_prime(r):
            is_circular = False
            break
    if is_circular:
        count += 1

print count
