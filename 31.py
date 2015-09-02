coins = [1, 2, 5, 10, 20, 50, 100, 200]
sols = []

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

different_ways_to_make([], 200)
print len(sols)
