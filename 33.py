# Backward compat to python 2
from __future__ import division

def gcd(a, b):
    """Calculate the Greatest Common Denominator of a & b
    Euclidean Algorithm
    http://codereview.stackexchange.com/questions/66450/simplify-a-fraction
    """
    while b:
        a, b = b, a % b
    return a

def simplify(n, d):
    # This can be simple because we know denominator > numerator > 0
    cd = gcd(n, d)
    return n // cd, d // cd
    
numerator_product = 1
denominator_product = 1

for numerator in range(10, 100):
    for denominator in range(10, 100):
        # Must be < 1
        if numerator >= denominator:
            continue

        # Ignore trivial
        if numerator % 10 == 0 and denominator % 10 == 0:
            continue

        # Change to arrays of 2 digits
        top = [numerator // 10, numerator % 10]
        bottom = [denominator // 10, denominator % 10]

        # try 'cancelling' each possible pair of digits
        for i in [0, 1]:
            for j in [0, 1]:
                if top[i] == bottom[j]:
                    # Avoid zero divisions
                    if top[1-i] == 0 or bottom[1-j] == 0:
                        continue
                    # See if removing these leads to the same fraction
                    if top[1-i] / bottom[1-j] == numerator / denominator:
                        numerator_product *= numerator
                        denominator_product *= denominator

n, d = simplify(numerator_product, denominator_product)
print d
                
