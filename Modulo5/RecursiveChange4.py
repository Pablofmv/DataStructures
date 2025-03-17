def recurvise_change(money,denominations):

    if money <= 0:
        return 0
    
    best = float("inf")

    for coin in denominations:

        if money >= coin:
            rest_coins = recurvise_change(money - coin, denominations)
            total_coins = rest_coins + 1

            if total_coins < best:
                best = total_coins
    
    return best

money = 14
denominations = [10,5,1]
print(recurvise_change(money,denominations))