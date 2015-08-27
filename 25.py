from math import log

a = b = 1
n = 2

while True:
    n += 1
    b += a
    a = b - a

    if log(b, 10) >= 999:
        break;

print n
        
