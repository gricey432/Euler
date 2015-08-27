contestants = range(2, 1000)

numerator = 1

while len(contestants) > 1:
    for contestant in contestants:
        # Remove even divisors
        if numerator % contestant == 0:
            contestants.remove(contestant)
            continue
        # Compare trailing sequences of results
        strnum = str(numerator / contestant)
        if len(strnum) > 20:
            for length in range(10, len(strnum)/2):
                a = strnum[-length:]
                b = strnum[-2*length:-length]
                if a == b:
                    contestants.remove(contestant)
                    break
    numerator *= 10

print contestants
