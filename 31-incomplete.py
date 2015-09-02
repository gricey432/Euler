coins = [1, 2, 5, 10, 20, 50, 100, 200]
cache = {
    1: 1
}
sols = []

def count_ways(amount):
    global coins, cache

    # Caching Answers
    if amount in cache:
        return cache[amount]

def make(amount, build):
    global coins, sols
    if amount == 0:
        if build not in sols:
            sols.append(build)
            return
    for i in range(len(coins)):
        if coins[i] > amount:
            continue

        new_build = list(build)
        new_build[i] += 1
        make(amount - coins[i], new_build)

def different_ways_to_make(build, remaining):
    global coins, sols
    if remaining == 0:
        build.sort()
        if build not in sols:
            #print build
            sols.append(build)
            return
    for coin in coins:
        if coin > remaining:
            continue
        
        build_copy = list(build)
        build_copy.append(coin)
        different_ways_to_make(build_copy, remaining - coin)

make(10, [0] * (len(coins) + 1))
print len(sols)
