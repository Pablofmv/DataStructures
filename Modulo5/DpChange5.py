def dp_change(money,coins):

    min_coins = [float("inf")] * (money + 1)
    min_coins[0] = 0

    for m in range(1,money+1):
        for coin in coins:
            if coin <= m:
                rest_coins = min_coins[m-coin] + 1

                if rest_coins < min_coins[m]:
                    min_coins[m] = rest_coins
    
    if min_coins[money] == float("inf"):
        return -1
    
    return min_coins[money]

money = 4
coins = [1,10,5]

print(dp_change(money,coins))