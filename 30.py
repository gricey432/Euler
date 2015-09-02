print sum(
    sum(
        pow(int(n), 5)
        for n in str(num)
    )
    for num in range(2, 200000)
    if sum(
        pow(int(n), 5)
        for n in str(num)
    ) == num
)

