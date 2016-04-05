pentagonals = [(n * (3 * n - 1) / 2) for n in range(1, 10000)]

best = 10000000

for i in pentagonals:
    for j in pentagonals:
        if i <= j:
            break

        if (i + j) not in pentagonals:
            continue

        if (i - j) not in pentagonals:
            continue

        print i, j
        if (i - j) < best:
            best = i - j

print best
