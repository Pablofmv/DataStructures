def greedy_change(money,denominations):
    denominations = sorted(denominations,reverse=True)
    Change = []

    while money > 0:
        for coin in denominations:
            if coin <= money:
                money -= coin
                Change.append(coin)
                break
    
    return Change

money = 10
denominations = [10,5,1]
print(greedy_change(money,denominations))
