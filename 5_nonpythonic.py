n = 20
while True:
    if (
        not n % 11
        and not n % 12
        and not n % 13
        and not n % 14
        and not n % 15
        and not n % 16
        and not n % 17
        and not n % 18
        and not n % 19
        and not n % 20
    ):
        break
    n += 20

print n
