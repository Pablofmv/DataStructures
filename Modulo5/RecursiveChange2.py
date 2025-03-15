def recursive_change(money,denominations):

    if money == 0:
        return 0
    
    best = float('inf')

    for coin in denominations:

        if money >= coin:

            coins_for_rest = recursive_change(money - coin, denominations)
            total_coins = coins_for_rest + 1

            if total_coins < best:
                best = total_coins
    
    return best

money = 12
denominations = [1,10,5]
print(recursive_change(money,denominations))