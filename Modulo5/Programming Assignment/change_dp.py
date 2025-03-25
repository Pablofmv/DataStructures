def change(money):
    # write your code here

    coins = [1,3,4]
    min_coins = [float("inf")] * (money + 1)
    min_coins[0] = 0

    for m in range(1, money+1):
        for coin in coins:
            if coin <= m:
                rest_coins = min_coins[m - coin] + 1

                if rest_coins < min_coins[m]:
                    min_coins[m] = rest_coins
    
    if min_coins[money] == float("inf"):
        return -1

    return min_coins[money]


if __name__ == '__main__':
    m = int(input())
    print(change(m))
