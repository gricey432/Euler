print sum(i if not i%3 or not i%5 else 0 for i in range(1000))
