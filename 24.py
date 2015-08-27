def permutations(items):
    if len(items) == 1:
        return items
    result = []
    for n in items:
        newitems = list(items)
        newitems.remove(n)
        perms = [n + p for p in permutations(newitems)]
        result += perms
    return result

perms = permutations([str(n) for n in range(10)])
print perms[999999]
