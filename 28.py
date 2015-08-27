total = 1
for layer in range(1,501):
    size = 2 * layer + 1
    total += size * size * 4 - sum([n * (size-1) for n in [1,2,3]])

print total
