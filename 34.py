import math

total = 0

for n in range(3, 1000000):
	if n == sum(math.factorial(int(c)) for c in str(n)):
		print n
		total += n
