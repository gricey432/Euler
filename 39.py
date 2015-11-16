counts = [0] * 1001

# this will count each triangle twice, but we don't care cause we only want the max
# not the actual count

def is_square(n):
  x = n // 2
  seen = set([x])
  while x * x != n:
    x = (x + (n // x)) // 2
    if x in seen: return False
    seen.add(x)
  return True

def isqrt(n):
    x = n
    y = (x + 1) // 2
    while y < x:
        x = y
        y = (x + n // x) // 2
    return x

for v in range(1, 1001):
    for h in range(1, 1001):
        v2 = v ** 2
        h2 = h ** 2
        if v + h > 1000:
            break
        elif not is_square(v2 + h2):
            continue
        else:
            p = v + h + isqrt(v2 + h2)
            if p > 1000:
                break
            counts[p] += 1

m = max(counts)
print [i for i, j in enumerate(counts) if j == m][0]
        
