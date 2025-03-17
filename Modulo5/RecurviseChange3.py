def RecurviseChange(money,denominations):

    if money <= 0:
        return 0
    
    best = float('inf')

    for coin in denominations:
        if coin <= money:
            rest_coins = RecurviseChange(money - coin, denominations)
            total_coins = rest_coins + 1

            if total_coins < best:
                best = total_coins
    
    return best

denominations = [15,2,1]
money = 17
print(RecurviseChange(money,denominations))