a = 999
b = 999
best_palindrome = 0

def is_palindrome(n):
    s = str(n)
    tens = len(s) - 1
    i = 0
    while i <= tens / 2:
        if not s[i] == s[tens - i]:
            return False
        i += 1
    return True
    

while a > 99:
    if is_palindrome(a * b):
        if a * b > best_palindrome:
            best_palindrome = a * b

    if b == 100:
        b = 999
        a -= 1
    else:
        b -= 1
    
print best_palindrome
    
