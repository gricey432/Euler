pandigital_products = []
pandigital_chars = [str(n) for n in range(1, 10)]

for multiplicand in range(1, 10000):
    max_multiplier = 100000 / multiplicand
    for multiplier in range(1, max_multiplier + 1):
        product = multiplicand * multiplier
        test_str = str(multiplicand) + str(multiplier) + str(product)
        if len(test_str) == len(pandigital_chars):
            if sorted(test_str) == pandigital_chars:
                pandigital_products.append(product)

print sum(list(set(pandigital_products)))
