collatz_cache = {}

def collatz_counter(n):
    global collatz_cache
    if n not in collatz_cache:
        if n == 1:
            collatz_cache[n] = 1
        elif n%2 == 0:
            collatz_cache[n] = collatz_counter(n / 2) + 1
        else:
            collatz_cache[n] = collatz_counter(3 * n + 1) + 1
    return collatz_cache[n]

longest_num = 0
longest_length = 0

for n in range(1, 1000000):
    length = collatz_counter(n)
    if length > longest_length:
        longest_length = length
        longest_num = n

print longest_num
