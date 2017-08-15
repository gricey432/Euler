from __future__ import division, print_function

highest_digital_sum = 0

for a in range(1, 101):
    for b in range(1, 101):
        n = a ** b
        digital_sum = 0
        while n:
            digital_sum += n % 10
            n //= 10
        highest_digital_sum = max(highest_digital_sum, digital_sum)

print(highest_digital_sum)
