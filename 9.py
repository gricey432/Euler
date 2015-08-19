for a in range(1, 501):
    for b in range(1, 501):
        c = 1000 - a - b
        if pow(a, 2) + pow(b, 2) == pow(c, 2):
            print a * b * c
            break
    else:
        continue
    break
        
