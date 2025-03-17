import time

def dp_change(money, coins):
    min_num_coins = [float("inf")] * (money + 1)
    min_num_coins[0] = 0

    for m in range(1,money+1):

        for coin in coins:
            if m >= coin:
                num_coins = min_num_coins[m-coin] + 1

                if num_coins < min_num_coins[m]:
                    min_num_coins[m] = num_coins
        
    if min_num_coins[money] == float("inf"):
        return -1

    return  min_num_coins[money]

money = 1
coins = [1,3,4]
start_time = time.time()
print(dp_change(money,coins))
end_time = time.time()
print(f"{end_time - start_time:.6f}")