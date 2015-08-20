fc = 0

def collatz_counter(n):
    global fc
    fc += 1
    if n == 1:
        return 1
    if n%2 == 0:
        return collatz_counter(n / 2) + 1
    return collatz_counter(3 * n + 1) + 1

longest_num = 0
longest_length = 0

for n in range(1, 1000000):
    length = collatz_counter(n)
    if length > longest_length:
        longest_length = length
        longest_num = n

print longest_num
