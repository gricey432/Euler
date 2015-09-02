def is_palindrome(n):
    s = str(n)
    tens = len(s) - 1
    i = 0
    while i <= tens / 2:
        if not s[i] == s[tens - i]:
            return False
        i += 1
    return True

total = 0

for n in range(1000000):
    if is_palindrome(n):
        base_2 = int(bin(n)[2:])
        if is_palindrome(base_2):
            total += n

print total
