square_sum = sum([pow(i, 2) for i in range(1, 101)])
sum_square = pow(sum([i for i in range(1, 101)]), 2)
print sum_square - square_sum
