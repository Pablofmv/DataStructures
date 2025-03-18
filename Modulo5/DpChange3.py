def dp_change(money,coins):

    min_coins = [float("inf")] * (money + 1)

    min_coins[0] = 0

    for m in range(1,money+1):
        for coin in coins:
            if coin <= m:
                total_coims = min_coins[m-coin] + 1

                if total_coims < min_coins[m]:
                    min_coins[m] = total_coims
    
    if min_coins[money] == float("inf"):
        return -1
    
    return min_coins[money]

money = 6
coins = [1,3,4]

print(dp_change(money,coins))


