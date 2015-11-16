coins = [1, 2, 5, 10, 20, 50, 100, 200]
target = 200

count = 0

def recursive_coin(prev_sum, coin_id):
    global coins, target, count
    value = coins[coin_id]
    for n in range(target / value + 1):
        new_sum = prev_sum + n * value
        if new_sum is target:
            count += 1
            return
        elif new_sum > target:
            return
        elif coin_id is len(coins) - 1:
            continue
        else:
            recursive_coin(new_sum, coin_id + 1)

recursive_coin(0, 0)
print count
