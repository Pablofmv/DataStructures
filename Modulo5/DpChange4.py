import time

def dp_changes(money,coins):

    min_coins = [float("inf")] * (money + 1)
    min_coins[0] = 0

    for m in range(1,money+1):
        for coin in coins:

            if coin <= m:
                total_coins = min_coins[m - coin] + 1

                if total_coins < min_coins[m]:
                    min_coins[m] = total_coins
    
    if min_coins[money] == float("inf"):
        return -1
    
    return min_coins[money]

money = 6
coins = [1,3,4]

start_time = time.time()
print(dp_changes(money,coins))
end_time = time.time()

print(f"{end_time - start_time:.6f}")