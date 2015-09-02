a = b = range(2, 101)

combos = [pow(an, bn) for an in a for bn in b]

unique_combos = list(set(combos))

print len(unique_combos)
